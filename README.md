



## memoryAnalyser.py
A convenient tool for memory forensics.

The script simply runs a (predefined) set of Volatility plugins on a given memory dump, concatenates the outputs in one .txt file for a (slightly) more convenient examination.

Tested on volatility_2.6_win64_standalone, which can be found here: [https://github.com/volatilityfoundation/volatility/releases](https://github.com/volatilityfoundation/volatility/releases)

Place the script in your Volatility folder (or change the path in the script). Edit the list of plugins to run ( # 2). An overview can be found here: [https://github.com/volatilityfoundation/volatility/wiki/Command-Reference](https://github.com/volatilityfoundation/volatility/wiki/Command-Reference) and here [https://downloads.volatilityfoundation.org/releases/2.4/CheatSheet_v2.4.pdf](https://downloads.volatilityfoundation.org/releases/2.4/CheatSheet_v2.4.pdf)

Open Power Shell in the working directory and run the script on your memory image e.g:

````
python ./memoryAnalyse.py ./evidence.mddramimage
````
When done, the terminal will print "Anlysis complete" and the .txt file (with the same name as the memory image) will now be available in the working directory. 


[![Download](https://custom-icon-badges.demolab.com/badge/Script:-memoryAnalyser.py-B58DAE?style=flat&logo=download&logoColor=white)](https://uc3bpr20.oddweb.io/artefacts/homey_pro_emmc/homey_pro_emmc_pre_experiment/HomeyProPre.E01)

![memoryANalyser.py](/media/ray-so-export.png)



`Until next time...`
<br>

  <a href="https://oddweb.io">
    <img src="media/oddscull_the_engineer.webp" alt="Logo" width="200">
  </a>