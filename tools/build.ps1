pyinstaller `
    --workpath ./build/build `
    --distpath ./build/install `
    --specpath ./build `
    --noconsole `
    -D `
    ./src/案例工程.py
    # -i ../resource/main.ico `
    # --key 'lolikonloli' `

# Copy-Item ./src/ui ./build/install/main -recurse -force

