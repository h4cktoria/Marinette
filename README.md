# Marinette

Cute, simple and open source shell

```text
Oo      oO                                                 
O O    o o               o                                 
o  o  O  O                                 O     O         
O   Oo   O                                oOo   oOo        
O        o .oOoO' `OoOo. O  'OoOo. .oOo.   o     o   .oOo. 
o        O O   o   o     o   o   O OooO'   O     O   OooO' 
o        O o   O   O     O   O   o O       o     o   O     
O        o `OoO'o  o     o'  o   O `OoO'   `oO   `oO `OoO' 
==========================================================
-16:17- Loading various systems...
-16:17- Checking various systems...
-16:17- Everything is loaded successfully
  Username as Host on 192.168.1.2 in /
% 
```

(Yes, I'm lazy to make screenshots)

Important note: this is **NOT A REAL HACKING TOOLKIT**! This has been made, works and will work only in the game called Grey Hack!

This repository is the only place where you can get Marinette without any risks. DON'T trust in-game websites!!!

Back to MVP state




## Table of contents

1.  [Description](#description)
2.  [Roadmap](#roadmap)
3.  [How to install?](#installation-guide)
4.  [How to contribute?](#contribution)
    -   [Themes](#contrib-themes)
    -   [Translations](#contrib-lang)
    -   [Bug report](#contrib-bugreport)
5.  [Frequently Asked Questions](#faq)
6.  [Other interesting projects](#similar-projects)
    -   [Shells](#similar-projects-shells)
    -   [Other](#similar-projects-other)
7.  [License](#license)
8.  [Thanks and Credits](#thanks-and-credits)




## Description <a name="description"></a>

Marinette is a [Shell](https://en.wikipedia.org/wiki/Shell_(computing)) without any fancy features like [Shell Expansions](https://www.gnu.org/software/bash/manual/html_node/Shell-Expansions.html), [Shell Scripting](https://en.wikipedia.org/wiki/Shell_script), [Pipelines](https://en.wikipedia.org/wiki/Pipeline_(Unix)) and so on. I've tried to make it as simple as I could, using few to no abstractions, allowing both the end users and myself to change it programmatically if needed. And I wouldn't say I've succeeded. =D

If you're a newbie then PLEASE DON'T USE MARINETTE OR ANY OTHER PREMADE HACKING TOOL! Hack by hand first, get a grip on the game mechanics, try to code something by yourself and have fun in general!




## Roadmap <a name="roadmap"></a>

These are what I plan to implement, in no particular order, as integratable programs(So that they are trivial to port into any other script):

-   Antivirus
-   Text editor
-   File manager
-   Task manager
-   Package manager
-   Network scanner
-   Users & Groups manager
-   Network cracker and manager




## How to install? <a name="installation-guide"></a>

1.  Clone the repository
2.  From the root of the project, run **scripts/install_marinette.py**. It'll create **install_marinette.src**. Copy it to the Code Editor, compile it, run the binary
3.  Go to **/home/guest/Sources/Marinette/src** and copy everything from [src](src) to here
4.  Change the stuff in **marilib.src**
    1.  From the root of the project, run **scripts/config_password.py** with the desired password. Set the value in **Config.password**
    2.  From the root of the project, run **scripts/config_identificator.py**. Set the value in **Config.identificator**
    3.  (Optionally) From the root of the project, run **scripts/config_available_languages.py**. Set the desired language in **Config.language**
    4.  (Optionally) From the root of the project, run **scripts/config_available_thenes.py**. Set the desired theme in **Config.theme**
5.  Compile **marinette.src**. Launch Marinette with `--password YOUR_PASSWORD_HERE` parameters. Congratulations!




## How to contribute? <a name="contribution"></a>

There are several ways you can contribute to Marinette


### Themes <a name="contrib-themes">

Fork, put your theme inside of [themes](themes), run [src_make_themeing.py](src/src_make_themeing.py), commit and open the pull request


### Translations <a name="contrib-lang">

NOT ACCEPTING USING THIS METHOD! I've forgot to change translation contribution with last commit and will do it later

Want to translate a lot locale entries for Marinette to be able to speak in your language for absolutely no reason and without getting paid? Nice! Fork the repository. You're looking for [localization.src](src/localization.src). Copy the English locale from here to any text editor, change the **_language** variable from English to the language of your choice and start translating! The rules are the following:

-   You're prohibited to translate anything in curly brackets caps. For example, you can't translate `{SESSION}`, `{HOST}`, `{SHELLS}`, etc
-   If you feel your language doesn't have an English terminology counterpart, just transliterate it. Examples of such terminology: "LocalHost", "Service", "Hash", "Crack", etc
-   Marinette's pronouns are she/her, so if your language has them, translate accordingly
-   Glued words CAN'T be translated as separate! For example, "PublicAddress" can't be translated as "Public Address" in your language

Once you're done, scroll to the bottom of the [localization.src](src/localization.src), make 4 new lines and append your locale after the latest one, commit and open the pull request


### Bug report <a name="contrib-bugreport">

Open up an issue and wait for my response




## Frequently Asked Questions <a name="faq"></a>


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




## Other interesting projects <a name="similar-projects"></a>

Another interesting projects that you should know about

If you want me to add your project, then open an issue and I'll add you as fast as I can! The exception is proprietary software


### Shells <a name="similar-projects-shells"></a>

-   [5hell](https://github.com/jhook777/5hell-for-Grey-Hack-the-Game) by Plu70. Keep in mind the github updates less frequently than the in-game site, so look for most up-to-date version in the game(As of 31 Jan 2024 the official in-game website is www.5hell.org)
-   [SeaShell](https://github.com/Tuna-Terps/SeaShell-greyhack-game) by Tuna Terps
-   [rocShell](https://github.com/rocketorbit/rocShell) by rocketorbit
-   [Lunar](https://github.com/cloverrfoxx/greyhack) by Clover if you are experienced enough to remove backdoor functionality, [Unclovered Lunarium](https://github.com/h4cktoria/unclovered-lunarium) by myself if you are not
-   [Project Pollux](https://github.com/SidiaDevelopment/greyhack-console) by Sidia
-   [Project p1an0Xshell](https://github.com/wh0wfg/greyscripts-p1an0) by Irtalhmu
-   [Project Vexxed](https://github.com/WizeWizard42/GreyHack-Vexxed) by WizeWizard
-   [OpenViper](https://github.com/cantemizyurek/viper-3.0) by SkidMall


### Other <a name="similar-projects-other"></a>

-   [MTX Framework](https://github.com/tuonux/mtx) by tuonux




## License <a name="license"></a>

Marinette is licensed under MIT No Attribution. See [here](LICENSE) for full details




## Thanks and Credits <a name="thanks-and-credits"></a>

Special thanks and credits goes to:

-   [Kurouzu](https://steamcommunity.com/profiles/76561198135838638) - for [Grey Hack](https://store.steampowered.com/app/605230/Grey_Hack/)
-   [Joe Strout](https://github.com/JoeStrout) - for [MiniScript](https://github.com/JoeStrout/miniscript)
-   [A lot of people](https://github.com/python/) - for [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
-   [Clover](https://github.com/cloverrfoxx) - for [Lunar](https://github.com/cloverrfoxx/greyhack), from where I've taken and adapted a lot of design choices
-   [Roupi](https://www.greyrepo.xyz/users/roupi) - for [Scan class module](https://www.greyrepo.xyz/posts/scan-class)
-   [Finko42](https://github.com/Finko42) - for [Encryption and Hashing algorithms](https://github.com/Finko42/GreyHack)
-   Ariavne - for allowing me to use their nickname as a command name(see `ariadne`)
-   [Guest](https://github.com/fmmaks666) - for Ukrainian translation and plugins implementation
-   [Simonize](https://github.com/Simoniko) - for color scheme(see `NoAuthV3Ocean` theme) and Polish translation

You are all awesome! Thank you a lot, Marinette wouldn't be what it is if it weren't for you people! <3

If I've somehow forgotten to mention you in here then accept my apologizes! Open an issue and I'll add you as fast as I can!
