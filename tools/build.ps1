pyinstaller `
    --workpath ./build/build `
    --distpath ./build/install `
    --specpath ./build `
    --noconsole `
    -D `
    ./src/main.py
    # -i ../resource/main.ico `
    # --key 'lolikonloli' `

# Copy-Item ./src/ui ./build/install/main -recurse -force

