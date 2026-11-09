#!/usr/bin/env bash
# move_labs_to_branches.sh
#
# Раскладывает лабораторные по отдельным веткам:
#   lab_1  -> содержит lab_01 (lab_02 из неё удаляется)
#   lab_2  -> содержит lab_02 (lab_01 из неё удаляется)
#   main   -> lab_01 и lab_02 удаляются
#
# История файлов сохраняется: ветки создаются от текущего origin/main,
# поэтому lab_01 остаётся в истории lab_1, lab_02 — в истории lab_2.
#
# Запуск (из корня клона репозитория):
#   bash scripts/move_labs_to_branches.sh           # сделать всё и запушить
#   DRY_RUN=1 bash scripts/move_labs_to_branches.sh # только показать, что будет сделано
#
# Скрипт безопасен для повторного запуска: уже готовые ветки он пропускает.

set -euo pipefail

REMOTE="${REMOTE:-origin}"
DRY_RUN="${DRY_RUN:-0}"
LAB1_DIR="lab_01"
LAB2_DIR="lab_02"
LAB1_BRANCH="lab_1"
LAB2_BRANCH="lab_2"

die() { echo "ОШИБКА: $*" >&2; exit 1; }
info() { echo "==> $*"; }
run() {
  if [ "$DRY_RUN" = "1" ]; then
    echo "    [dry-run] $*"
  else
    "$@"
  fi
}

# --- проверки -------------------------------------------------------------
git rev-parse --git-dir >/dev/null 2>&1 || die "запускайте скрипт из git-репозитория"
[ -z "$(git status --porcelain)" ] || die "рабочее дерево не чистое — сначала закоммитьте или спрячьте изменения (git stash)"

info "получаю свежие данные с $REMOTE"
git fetch "$REMOTE" --prune

if git show-ref --verify --quiet "refs/remotes/$REMOTE/main"; then
  MAIN="main"
elif git show-ref --verify --quiet "refs/remotes/$REMOTE/master"; then
  MAIN="master"
else
  die "не нашёл ветку main/master на $REMOTE"
fi
BASE="$REMOTE/$MAIN"
info "базовая ветка: $BASE"

# --- утилиты --------------------------------------------------------------
# Возвращает 0, если в origin/<branch> есть указанный каталог
remote_has_dir() { # $1=branch $2=dir
  git ls-tree -r --name-only "$REMOTE/$1" | grep -q "^$2/"
}

# Создаёт ветку от $BASE, удаляет из неё ненужный каталог, пушит.
make_lab_branch() { # $1=branch $2=dir_to_keep $3=dir_to_remove
  local branch="$1" keep="$2" drop="$3"

  if git show-ref --verify --quiet "refs/remotes/$REMOTE/$branch"; then
    info "ветка $branch уже есть на $REMOTE — пропускаю создание"
    if remote_has_dir "$branch" "$keep"; then
      info "  в $branch есть $keep — ок"
    else
      echo "  ВНИМАНИЕ: в $branch нет каталога $keep, проверьте вручную" >&2
    fi
    return 0
  fi

  if ! remote_has_dir "$MAIN" "$keep"; then
    echo "  ВНИМАНИЕ: в $MAIN нет каталога $keep — создавать нечего, пропускаю" >&2
    return 0
  fi

  info "создаю ветку $branch от $BASE (с $keep)"
  run git checkout -q -b "$branch" "$BASE"

  if remote_has_dir "$MAIN" "$drop"; then
    info "  удаляю $drop из $branch (он останется в ветке для другой лабы)"
    run git rm -r -q "$drop"
    run git commit -q -m "$branch: оставить только $keep ($drop перенесён в отдельную ветку)"
  fi

  run git push -u "$REMOTE" "$branch"
}

# --- 1. ветка lab_1 и ветка lab_2 -----------------------------------------
make_lab_branch "$LAB1_BRANCH" "$LAB1_DIR" "$LAB2_DIR"
[ "$DRY_RUN" = "1" ] || git checkout -q "$MAIN"

make_lab_branch "$LAB2_BRANCH" "$LAB2_DIR" "$LAB1_DIR"
[ "$DRY_RUN" = "1" ] || git checkout -q "$MAIN"

# --- 2. чистим main -------------------------------------------------------
info "перехожу на локальную $MAIN и синхронизируюсь с $BASE"
run git checkout -q "$MAIN"
run git pull -q --ff-only "$REMOTE" "$MAIN"

dirs_to_remove=()
for d in "$LAB1_DIR" "$LAB2_DIR"; do
  if [ -e "$d" ] || git ls-files --error-unmatch "$d" >/dev/null 2>&1; then
    dirs_to_remove+=("$d")
  fi
done

if [ ${#dirs_to_remove[@]} -eq 0 ]; then
  info "в $MAIN уже нет $LAB1_DIR/$LAB2_DIR — чистить нечего"
else
  info "удаляю из $MAIN: ${dirs_to_remove[*]}"
  run git rm -r -q "${dirs_to_remove[@]}"
  run git commit -q -m "Удалить ${dirs_to_remove[*]} из main (перенесены в ветки $LAB1_BRANCH / $LAB2_BRANCH)"
  run git push "$REMOTE" "$MAIN"
fi

info "готово. Итоговое состояние веток:"
git ls-tree -r --name-only "$REMOTE/$LAB1_BRANCH" | sed "s|^|  $LAB1_BRANCH/|"
echo "  ---"
git ls-tree -r --name-only "$REMOTE/$LAB2_BRANCH" | sed "s|^|  $LAB2_BRANCH/|"
echo "  ---"
git ls-tree -r --name-only "$REMOTE/$MAIN" | sed "s|^|  $MAIN/|"

if [ "$DRY_RUN" = "1" ]; then
  echo "(это был dry-run: ничего не изменено и не отправлено)"
fi
