python -m nuitka `
    --nofollow-imports `
    --plugin-enable=pyside6 `
    --show-progress `
    --show-memory `
    --output-dir=./build/suitka_build `
    --windows-disable-console `
    .\src\main.py `
    --standalone `
    --include-package-data="qt_material"
