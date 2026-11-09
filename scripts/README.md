# Раскладка лабораторных по веткам

Задача: `lab_01` → ветка `lab_1`, `lab_02` → ветка `lab_2`, из `main` обе папки убрать,
но так, чтобы файлы остались доступны в других ветках и в истории git.

## Вариант 1 — скрипт (рекомендуется)

Из корня клона:

```bash
DRY_RUN=1 bash scripts/move_labs_to_branches.sh   # показать, что будет сделано
bash scripts/move_labs_to_branches.sh             # сделать и запушить
```

Что он делает:

1. `git fetch origin` и берёт `origin/main` как базу.
2. Создаёт ветку `lab_1` от `origin/main`, удаляет из неё `lab_02`, коммитит и пушит.
3. Создаёт ветку `lab_2` от `origin/main`, удаляет из неё `lab_01`, коммитит и пушит.
   (`lab_01` при этом **остаётся** в `lab_1`, `lab_02` — в `lab_2`.)
4. В `main` удаляет `lab_01` и `lab_02` и пушит.

Скрипт можно запускать повторно: уже существующие ветки он только проверяет,
а если в `main` чистить нечего — просто выходит.

## Вариант 2 — вручную

```bash
git fetch origin
git checkout -b lab_1 origin/main
git rm -r lab_02
git commit -m "lab_1: оставить только lab_01"
git push -u origin lab_1

git checkout -b lab_2 origin/main
git rm -r lab_01
git commit -m "lab_2: оставить только lab_02"
git push -u origin lab_2

git checkout main
git pull --ff-only origin main
git rm -r lab_01 lab_02
git commit -m "Удалить lab_01 и lab_02 из main (перенесены в lab_1 / lab_2)"
git push origin main
```

## Почему файлы не теряются

Ветки создаются от текущего `main`, поэтому коммит, где лежат обе папки, —
предок и `lab_1`, и `lab_2`. Папки не удаляются из истории, они просто
перестают быть видны в «последней» версии `main`.

- Посмотреть старую версию файла: `git show origin/main~1:lab_01/REPORT.md`
- Вернуть папку в `main` при необходимости:
  `git checkout origin/main~1 -- lab_01`
- Список файлов ветки: `git ls-tree -r --name-only origin/lab_1`

## Замечания

- Ветки `lab_1`/`lab_2` в репозитории сейчас отсутствуют — скрипт создаст их с нуля.
- Если имена нужны другие (`lab_01`/`lab_02` вместо `lab_1`/`lab_2`), поменяйте
  переменные `LAB1_BRANCH`/`LAB2_BRANCH` в начале скрипта или выполните команды из варианта 2.
- `requirements.txt` и `.gitignore` остаются во всех трёх ветках — они общие для проекта.
- Если ветка `main` защищена (branch protection), push в неё из скрипта не пройдёт —
  тогда шаг очистки `main` нужно оформить отдельным PR.
