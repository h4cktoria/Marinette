# Marinette

Cute, simple and open source shell

Screenshots TODO

Important note: this is **NOT A REAL HACKING TOOLKIT**! This has been made, works and will work only in the game called Grey Hack!

This repository is the only place where you can get Marinette without any risks. DON'T trust in-game websites!!!




## Table of contents

1.  [Description](#description)
2.  [How to install?](#how-to-install)
3.  [How to contribute?](#how-to-contribute)
    -   [Themes](#themes)
    -   [Translations](#translations)
    -   [Bug report](#bug-report)
    -   [Code contribution](#code-contribution)
4.  [Frequently Asked Questions](#frequently-asked-questions)
5.  [Other interesting projects](#other-interesting-projects)
    -   [Shells](#shells)
    -   [Other](#other)
6.  [License](#license)
7.  [Thanks and Credits](#thanks-and-credits)




## Description

Marinette is a [Shell](https://en.wikipedia.org/wiki/Shell_(computing)) without any fancy features like [Shell Expansions](https://www.gnu.org/software/bash/manual/html_node/Shell-Expansions.html), [Shell Scripting](https://en.wikipedia.org/wiki/Shell_script), [Pipelines](https://en.wikipedia.org/wiki/Pipeline_(Unix)) and so on. I've tried to make it as simple as I could, using only structured programming, allowing the end users to change it programmatically if needed. And I wouldn't say I've succeeded. =D

Core(but not only!) features of Marinette:

-   Simple and source-leak secure compile-time configuration
-   [Defensive programmed](https://en.wikipedia.org/wiki/Defensive_programming) and won't crash if you misuse any command in any way
-   Fully translatable except for built-ins errors

Please read! If you're a newbie then PLEASE DON'T USE MARINETTE OR ANY OTHER PREMADE HACKING TOOL! Hack by hand first, get a grip on the game mechanics, try to code something by yourself and have fun in general!




## How to install?

1.  Clone the repository
2.  From the root of the project, run **scripts/install_marinette.py**. It'll create **install_marinette.src**. Copy it to the Code Editor, compile it and run the binary
3.  Copy everything from [src](src) to **/home/guest/Sources/Marinette/src**
4.  Change configuration in **marinette.src**
    1.  From the root of the project, run **scripts/config_password.py** with the desired password. Set the value in **Config.password**
    2.  From the root of the project, run **scripts/config_identificator.py**. Set the value in **Config.identificator**
    3.  (Optionally) From the root of the project, run **scripts/config_available_languages.py**. Set the desired language in **Config.language**
    4.  (Optionally) From the root of the project, run **scripts/config_available_themes.py**. Set the desired theme in **Config.theme**
5.  Compile **marinette.src**. Launch Marinette with `--password {YOUR_PASSWORD}` parameters. Congratulations!




## How to contribute?

In the current state, I REALLY don't recommend you to contribute to Marinette as it's far from being complete. Anyway...

There are several ways you can contribute to Marinette


### Themes

Fork, put your theme inside of [themes](themes), run [install_marinette.py](scripts/install_marinette.py), commit and open the pull request


### Translations

Want to translate a lot locale entries for Marinette to be able to speak in your language for absolutely no reason and without getting paid? Nice! Fork the repository. You're looking for [locales](locales). Copy the English locale from here to any text editor, change the **_language** variable from English to the language of your choice and start translating! The rules are the following:

-   You're prohibited to translate anything in curly brackets caps. For example, you can't translate `{SESSION}`, `{HOST}`, `{SHELLS}`, etc
-   If you feel your language doesn't have an English terminology counterpart, just transliterate it. Examples of such terminology: "LocalHost", "Service", "Hash", "Crack", etc
-   Marinette's pronouns are she/her, so if your language has them, translate accordingly
-   Glued words CAN'T be translated as separate! For example, "PublicAddress" can't be translated as "Public Address" in your language

Once you're done, put your locale file into [locales](locales), run [install_marinette.py](scripts/install_marinette.py), commit and open the pull request


### Bug report

Open up an issue and wait for my response


### Code contribution

PLEASE MAKE SURE YOU UNDERSTAND MOST OF THE MINISCRIPT IMPLICIT BEHAVIOUR BEFORE MAKING A PULL REQUEST! This includes, but not limits to, the understanding of:

-   Behaviour of `range()`
-   How base class and it's instances behave
-   How different default routine arguments behave
-   Functions, list items and map items references
-   Scoping and data encapsulation

If you understand these, you won't question most of the design choices

Now that you're sure you know anything needed, have a look at these ~simple~ conventions:

-   OOP is PROHIBITED! Maps are structures or namespaces AND NOTHING MORE! No `self`, `super`, `.classID`, `new` and any other OOP mechanic
-   Compare built-in types with `isa`, Grey Hack objects with `typeof()`
-   Name everything with camelCase; structures, namespaces and locale entries with PascalCase
-   After each source change, run [install_marinette.py](scripts/install_marinette.py)
-   Don't reinvent the wheel! If the algorithm you want to use is already defined in [portable.src](src/portable.src), you MUST use it!
-   Before making a pull request, pull origin
-   Define locales in [english.src](locales/english.src) first, then in your locale file AND PLEASE DON'T TOUCH [localization.src](src/localization.src)!!!
-   Follow locale entries naming conventions described below

Locale naming conventions:
-   Prefix **Log** if entry is used in `Console.log()`: `Locales.LogExampleEntry[_language] = "Example translation"`
-   Prefix **Warning** if entry is used in `Console.warning()`: `Locales.WarningExampleEntry[_language] = "Example translation"`
-   Prefix **Error** if entry is used in `Console.error()`: `Locales.ErrorExampleEntry[_language] = "Example translation"`
-   Prefix command name and postfix **Header** if entry is used in table headers(`format_columns()` or `formatColumnsColored()`): `Locales.CommandNameExampleEntryHeader[_language] = "Example translation"`
-   For any other situation, prefix with command name IF the entry is specific to that command. If it's not, then prefix whatever you feel neccessary




## Frequently Asked Questions


**Q: Why on earth would you call a computer program with a human name?**

**A**: Never ask a Woman Her age, a Man, His salary, and Hacktoria - about Their programmes' names

Seriously, though, because everything made with love should be named as a human being


**Q: Why would you create yet another shell when there are already dozens of them?**

**A**: Because all shells lack something that I want and I have wanted something made by myself


**Q: When will you finally update?**

**A**: When I have time and will to do that


**Q: Why did you choose MIT-0 as a License?**

**A**: TL;DR: Best for the players' and developers' freedom

I've figured no one cares about license of your application in Grey Hack, so I've decided I want to give users complete freedom over Marinette. You've got her from github? You're free to do whatever you want with her. You've hacked another player and stealen the sources? You're free to do whatever you want. You've got the sources by exploiting a game? Yes, you guessed it, you're still free to do whatever you want. Full source availability also means I'll try my best so that it's leakage doesn't mean a game over for the user


**Q: Why the hell you're using custom sorting algorithms?**

**A**: Because built-in sort's impossible to perform with a predicate(Unless I'm missing something. If that's the case, open up a pull request)




## Other interesting projects

Another interesting projects that you should know about

If you want me to add your project, then open an issue and I'll add you as fast as I can! The exception is proprietary software


### Shells

-   [5hell](https://github.com/jhook777/5hell-for-Grey-Hack-the-Game) by Plu70. Keep in mind the github updates less frequently than the in-game site, so look for most up-to-date version in the game(As of 31 Jan 2024 the official in-game website is www.5hell.org)
-   [SeaShell](https://github.com/Tuna-Terps/SeaShell-greyhack-game) by Tuna Terps
-   [rocShell](https://github.com/rocketorbit/rocShell) by rocketorbit
-   [Lunar](https://github.com/cloverrfoxx/greyhack) by Clover if you are experienced enough to remove backdoor functionality, [Unclovered Lunarium](https://github.com/h4cktoria/unclovered-lunarium) by myself if you are not
-   [Project Pollux](https://github.com/SidiaDevelopment/greyhack-console) by Sidia
-   [Project p1an0Xshell](https://github.com/wh0wfg/greyscripts-p1an0) by Irtalhmu
-   [Project Vexxed](https://github.com/WizeWizard42/GreyHack-Vexxed) by WizeWizard
-   [OpenViper](https://github.com/cantemizyurek/viper-3.0) by SkidMall


### Other

-   [MTX Framework](https://github.com/tuonux/mtx) by tuonux




## License

Marinette is licensed under MIT No Attribution. See [here](LICENSE) for full details




## Thanks and Credits

Special thanks and credits goes to:

-   [Kurouzu](https://steamcommunity.com/profiles/76561198135838638) - for [Grey Hack](https://store.steampowered.com/app/605230/Grey_Hack/)
-   [Joe Strout](https://github.com/JoeStrout) - for [MiniScript](https://github.com/JoeStrout/miniscript)
-   [A lot of people](https://github.com/python/) - for [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
-   [Clover](https://github.com/cloverrfoxx) - for [Lunar](https://github.com/cloverrfoxx/greyhack), from where I've taken and adapted a lot of design choices
-   [Roupi](https://www.greyrepo.xyz/users/roupi) - for [Scan class module](https://www.greyrepo.xyz/posts/scan-class)
-   [Finko42](https://github.com/Finko42) - for [Encryption and Hashing algorithms](https://github.com/Finko42/GreyHack)
-   Ariavne - for allowing me to use their nickname as a command name(see `ariadne`)
-   [Guest](https://github.com/fmmaks666) - for Ukrainian translation and plugins implementation(which didn't get into Marinette because of how hard it is to make it SECURE)
-   [Simonize](https://github.com/Simoniko) - for color scheme(see `NoAuthV3Ocean` [theme](themes/nav3ocean.src)) and Polish translation
-   [Olipro](https://github.com/Olipro) - for making Omni, from leaked version of which I've ~stealen~ borrowed a color scheme(see `Omni` [theme](themes/omni.src))
-   [Volk](https://github.com/EntitySeaker) - for making Viper, from leaked version of which I've ~stealen~ borrowed a color scheme(see `Viper` [theme](themes/viper.src))

You are all awesome! Thank you a lot, Marinette wouldn't be what it is if it weren't for you people! <3

If I've somehow forgotten to mention you in here then accept my apologizes! Open an issue and I'll add you as fast as I can!
