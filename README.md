# Pressbook Similarity

Early exploration and experimentation with using automated text-similarity tools to assess how newspapers in the US drew upon the Pressbooks and other publicity materials shared by major movie studios.

- Newspaper data from the [Library of Congress Chronicling America]('https://chroniclingamerica.loc.gov/ocr/') collection
- Pressbooks from the [Media History Digital Library]('https://mediahistoryproject.org') collections

## Library Dependencies
Using a bunch of external python libraries. I'm trying my best to track them all in requirements.txt so that you can install everything with:

`pip install -r requirements.txt`

or possibly 

`python3 -m pip install -r requirements.txt`
(if you local Python environment is as malformed as mine is...)

## Downloading MHDL Pressbooks

The `mhdl-downlad.py` file will download items from the 'mediahistory' collection on the Internet Archive that match 'format: Pressbooks'

Currently I have it set up to only download the .txt files, and to drop them all into the 'mhdl-pressbooks' directory. 

It will also create a CSV file with some basic item metadata - this will be useful when automating similarity detection

## Internal Similarity

Once you've downloaded a bunch of Pressbook txt files, you can use the `mhdl-internal-similarity.py` script to run some basic tests of how similar the pressbooks are to one another.

NOTE: I am not using any stopwords or other quality control - so the "Scanned for the MHDL" at the end of every scan _will_ be counted as similar text.

This script will calculate Euclidean Distance and Cosine Distance for each of the files and print basic tables with this information. Inside the script, there is a line where you can set `comparison_target`, which is an identifier for a pressbook that you'd like to compare all the others to.

For example, here is similarity data for `pressbook-black-heat`:

### Euclidian Distance

```
EUCLIDEAN DISTANCES
                                                    pressbook-col-casino-royale  pressbook-col-the-big-sombrero  pressbook-col-everythings-ducky  ...  pressbook-coffy  pressbook-col-the-ambushers  pressbook-col-apache-ambush
pressbook-col-casino-royale                                            0.000000                      651.419987                       577.663397  ...       579.115705                   609.276620                   580.473944
pressbook-col-the-big-sombrero                                       651.419987                        0.000000                       346.616503  ...       355.056334                   427.083130                   345.218771
pressbook-col-everythings-ducky                                      577.663397                      346.616503                         0.000000  ...       177.988764                   301.458123                   161.675601
pressbook-col-china-venture                                          579.101891                      353.410526                       171.662459  ...       186.959889                   307.309290                   167.233370
pressbook-col-the-doolins-of-oklahoma                                590.914545                      378.589487                       237.050628  ...       244.002049                   345.904611                   229.189878
pressbook-col-the-cowboy-and-the-indians                             672.095975                      242.600495                       382.183202  ...       387.378368                   453.097120                   377.461256
pressbook-col-the-30-foot-bride-of-candy-rock                        582.134005                      346.992795                       162.163498  ...       174.421902                   298.100654                   160.099969
pressbook-col-murderers-row                                          599.287076                      401.953977                       261.411553  ...       271.506906                   219.665655                   261.252751
pressbook-black-heat                                                 573.331492                      332.501128                       125.666225  ...       136.959848                   284.971928                   119.369175
pressbook-col-the-black-arrow                                        636.524941                      446.929525                       330.458772  ...       324.584350                   412.446360                   323.808585
pressbook-col-dead-heat-on-a-merry-go-round                          584.579336                      363.762285                       195.176843  ...       202.459873                   317.286936                   194.332190
pressbook-col-the-happening                                          600.474812                      391.548209                       246.002033  ...       249.276954                   349.093111                   244.454495
pressbook-col-adventures-in-silverado                                594.511564                      373.679007                       222.227361  ...       215.951383                   333.304665                   213.302602
pressbook-col-the-brave-bulls                                        641.626059                      447.432677                       334.037423  ...       328.068590                   411.555586                   331.366866
pressbook-book-of-numbers                                            579.366033                      354.072027                       176.397279  ...       183.111988                   303.412261                   173.985632
pressbook-cleopatra-jones                                            580.684940                      359.965276                       187.946801  ...       191.864536                   313.047920                   185.156690
pressbook-col-the-flying-missile                                     624.050479                      426.120875                       291.821863  ...       306.835461                   380.369557                   294.589545
pressbook-col-flight-lieutenant                                      573.376839                      334.052391                       130.682822  ...       147.363496                   285.959787                   123.923363
pressbook-col-guess-whos-coming-to-dinner                            608.602498                      400.193703                       276.257127  ...       284.211189                   367.827405                   279.340294
pressbook-col-how-to-save-a-marriage-and-ruin-y...                   595.297405                      383.897122                       233.173755  ...       242.775617                   311.975961                   232.952785
pressbook-col-combat-squad                                           577.679842                      341.446921                       146.986394  ...       159.840546                   293.155249                   140.541809
pressbook-blacula                                                    581.326070                      359.874978                       195.971937  ...       176.830427                   318.483909                   194.283298
pressbook-col-rage                                                   583.753373                      358.566591                       190.354932  ...       201.923253                   313.531498                   184.070639
pressbook-col-gunning-for-vengeance                                  569.879812                      331.715239                       129.011627  ...       143.680200                   286.312766                   120.702113
pressbook-col-galloping-thunder                                      569.702554                      331.591616                       130.030766  ...       145.712045                   286.797838                   122.543870
pressbook-col-lost-command                                           598.270006                      394.069791                       249.507515  ...       255.483855                   347.578768                   249.208748
pressbook-col-kiss-the-girls-and-make-them-die                       583.329238                      371.064684                       207.248643  ...       218.837840                   308.446106                   207.169013
pressbook-col-anzio                                                  579.338416                      369.920262                       204.347743  ...       203.081265                   319.341510                   201.268477
pressbook-col-that-man-in-istanbul                                   573.467523                      340.686073                       146.935360  ...       160.480528                   288.899637                   145.275600
pressbook-bamboo-gods-and-iron-men                                   571.148842                      335.647136                       133.364163  ...       128.872030                   285.175385                   129.448832
pressbook-col-alvarez-kelly                                          584.863232                      372.447312                       214.392164  ...       222.715065                   323.454788                   209.315551
pressbook-change-of-mind                                             583.481791                      352.895169                       175.328264  ...       181.664526                   309.675637                   171.379695
pressbook-col-death-of-a-salesman                                    714.918877                      544.671461                       455.668739  ...       459.231968                   517.009671                   456.235685
pressbook-col-the-big-gusher                                         578.863542                      342.089170                       150.166574  ...       162.542302                   295.937493                   140.167757
pressbook-col-georgy-girl                                            607.370562                      412.214750                       275.238079  ...       280.381882                   366.945500                   276.414544
pressbook-coffy                                                      579.115705                      355.056334                       177.988764  ...         0.000000                   307.956166                   173.040458
pressbook-col-the-ambushers                                          609.276620                      427.083130                       301.458123  ...       307.956166                     0.000000                   300.649297
pressbook-col-apache-ambush                                          580.473944                      345.218771                       161.675601  ...       173.040458                   300.649297                     0.000000

[38 rows x 38 columns]



TOP 5 TEXTS THAT ARE MOST SIMILAR TO pressbook-black-heat:
pressbook-col-gunning-for-vengeance    65.452273
pressbook-col-galloping-thunder        68.774995
pressbook-bamboo-gods-and-iron-men     69.455021
pressbook-col-flight-lieutenant        70.171219
pressbook-col-combat-squad             97.247108
Name: pressbook-black-heat, dtype: float64
                                                                                 title                          creator  year
pressbook-col-gunning-for-vengeance  Gunning for Vengeance (Columbia Pictures Press...                Columbia Pictures  1946
pressbook-col-galloping-thunder      Galloping Thunder (Columbia Pictures Pressbook...                Columbia Pictures  1946
pressbook-bamboo-gods-and-iron-men   Bamboo Gods and Iron Men (American Internation...  American International Pictures  1974
pressbook-col-flight-lieutenant      Flight Lieutenant (Columbia Pictures Pressbook...                Columbia Pictures  1942
pressbook-col-combat-squad            Combat Squad (Columbia Pictures Pressbook, 1953)                Columbia Pictures  1953

**********

```

### Cosine Distance

```
COSINE DISTANCES
                                                    pressbook-col-casino-royale  pressbook-col-the-big-sombrero  ...  pressbook-col-the-ambushers  pressbook-col-apache-ambush
pressbook-col-casino-royale                                            0.000000                        0.959851  ...                     0.881106                     0.959082
pressbook-col-the-big-sombrero                                         0.959851                        0.000000  ...                     0.957838                     0.953360
pressbook-col-everythings-ducky                                        0.924767                        0.945240  ...                     0.942817                     0.964348
pressbook-col-china-venture                                            0.925278                        0.976351  ...                     0.962518                     0.946601
pressbook-col-the-doolins-of-oklahoma                                  0.900381                        0.926895  ...                     0.965731                     0.925354
pressbook-col-the-cowboy-and-the-indians                               0.969090                        0.236023  ...                     0.951283                     0.935883
pressbook-col-the-30-foot-bride-of-candy-rock                          0.968271                        0.959351  ...                     0.925055                     0.981081
pressbook-col-murderers-row                                            0.898955                        0.963620  ...                     0.341409                     0.968766
pressbook-black-heat                                                   0.944301                        0.953408  ...                     0.961428                     0.976451
pressbook-col-the-black-arrow                                          0.939996                        0.964663  ...                     0.959223                     0.931639
pressbook-col-dead-heat-on-a-merry-go-round                            0.922267                        0.959218  ...                     0.931596                     0.957300
pressbook-col-the-happening                                            0.928628                        0.960229  ...                     0.939862                     0.960079
pressbook-col-adventures-in-silverado                                  0.943945                        0.948768  ...                     0.951122                     0.925464
pressbook-col-the-brave-bulls                                          0.951460                        0.954604  ...                     0.940823                     0.964924
pressbook-book-of-numbers                                              0.917373                        0.957907  ...                     0.905269                     0.950090
pressbook-cleopatra-jones                                              0.913201                        0.969770  ...                     0.943017                     0.973565
pressbook-col-the-flying-missile                                       0.945299                        0.968847  ...                     0.918088                     0.949891
pressbook-col-flight-lieutenant                                        0.937904                        0.957010  ...                     0.947165                     0.966287
pressbook-col-guess-whos-coming-to-dinner                              0.911035                        0.900261  ...                     0.916439                     0.967811
pressbook-col-how-to-save-a-marriage-and-ruin-y...                     0.920895                        0.953676  ...                     0.774484                     0.954731
pressbook-col-combat-squad                                             0.963453                        0.978483  ...                     0.956689                     0.965565
pressbook-blacula                                                      0.904894                        0.939769  ...                     0.947689                     0.978322
pressbook-col-rage                                                     0.928371                        0.948014  ...                     0.933090                     0.924978
pressbook-col-gunning-for-vengeance                                    0.872501                        0.923898  ...                     0.969490                     0.946640
pressbook-col-galloping-thunder                                        0.872267                        0.914718  ...                     0.965378                     0.948022
pressbook-col-lost-command                                             0.911244                        0.958977  ...                     0.915082                     0.961808
pressbook-col-kiss-the-girls-and-make-them-die                         0.898980                        0.970321  ...                     0.837128                     0.979012
pressbook-col-anzio                                                    0.881123                        0.976811  ...                     0.920168                     0.959540
pressbook-col-that-man-in-istanbul                                     0.909448                        0.949419  ...                     0.888249                     0.963933
pressbook-bamboo-gods-and-iron-men                                     0.897367                        0.956729  ...                     0.907674                     0.971680
pressbook-col-alvarez-kelly                                            0.897962                        0.955882  ...                     0.906724                     0.930188
pressbook-change-of-mind                                               0.950703                        0.955181  ...                     0.961810                     0.941117
pressbook-col-death-of-a-salesman                                      0.968051                        0.962104  ...                     0.957105                     0.977124
pressbook-col-the-big-gusher                                           0.971061                        0.974663  ...                     0.975913                     0.926823
pressbook-col-georgy-girl                                              0.912110                        0.969640  ...                     0.926167                     0.978357
pressbook-coffy                                                        0.916965                        0.968961  ...                     0.944521                     0.950156
pressbook-col-the-ambushers                                            0.881106                        0.957838  ...                     0.000000                     0.960355
pressbook-col-apache-ambush                                            0.959082                        0.953360  ...                     0.960355                     0.000000

[38 rows x 38 columns]
TOP 5 TEXTS THAT ARE MOST SIMILAR TO pressbook-black-heat:
pressbook-bamboo-gods-and-iron-men             0.725294
pressbook-coffy                                0.834409
pressbook-col-the-black-arrow                  0.840341
pressbook-blacula                              0.840409
pressbook-col-dead-heat-on-a-merry-go-round    0.897347
Name: pressbook-black-heat, dtype: float64



                                                                                         title                          creator  year
pressbook-bamboo-gods-and-iron-men           Bamboo Gods and Iron Men (American Internation...  American International Pictures  1974
pressbook-coffy                              Coffy (American International Pictures Pressbo...  American International Pictures  1973
pressbook-col-the-black-arrow                The Black Arrow (Columbia Pictures Pressbook, ...                Columbia Pictures  1948
pressbook-blacula                            Blacula (American International Pictures Press...  American International Pictures  1972
pressbook-col-dead-heat-on-a-merry-go-round  Dead Heat on a Merry-Go-Round (Columbia Pictur...                Columbia Pictures  1966
```


---

# find-newspapers

This is more of an all-in-one script that begins to do some basic comparisons with actual data from the LOC collection. It will read a list of Pressbooks (formatted as Internet Archive identifiers) and use those to search Chronicling America for newspaper pages that were published just a few years after the Pressbook. Next, it does cosine and euclidean similarity measurements for the text files and saves this data to CSV files.

*note* Currently, the script _only_ works with the first page of LOC results - meaning that it's only comparing ~20 newspaper pages, and is nowhere near comprehensive. Many queries have hundreds of thousands of pages, so this is mainly just a proof of concept of the workflow that will be necessary. We'll need to make this as efficient as possible and then distribute the workload

*note #2* The script is just using the raw OCR text from the MHDL and LOC. The quality of the results can likely be improved by doing some basic OCR normalization and incorporating fuzzy matching. For example things for us to consider:
- we need to deal with line breaks
- hyphenation (over line breaks) is also a problem. Words that match may not be recognized depending on how the newspaper layout wrapped the text
- We should probably omit the last page of text from the Pressbook - since this is generally the "acknowledgements" page that is added in


## Input Lists
Currently, I'm using a file named `pressbook-search-list.txt` to list IA identifiers. I'm only running this with a small handful of Pressbooks for now.

## Query range
THe script has a line to specify how many years beyond the Pressbook publication to search for. I set it for 5, but that could (should) be finetuned to a likely range that newspapers might still be writing anything about a given film.


### But does it work?

Based on my initial testing, this seems to be a good starting workflow. And, I think it's going to work for what we want to do. In my initial testing, I was seeing _very_ dissimilar texts. For the cosine distance (which ranges from 0-1), I would often see a comparison around 0.8, meaning that the newspaper pages were not similar to the pressbook at all. 

But one Pressbook [pressbook-col-the-flying-missile](https://archive.org/details/pressbook-col-the-flying-missile) returned some slightly lower scores.

```
TOP 5 TEXTS THAT ARE MOST SIMILAR TO pressbook-col-the-flying-missile_djvu:
lccn_sn91069201_1950-02-04_ed-1_seq-7    0.521970
lccn_sn91069201_1950-02-04_ed-1_seq-8    0.526317
lccn_sn91069201_1950-02-11_ed-1_seq-7    0.561699
lccn_sn91069201_1950-02-11_ed-1_seq-5    0.603617
lccn_sn91069201_1950-02-11_ed-1_seq-6    0.610945
Name: pressbook-col-the-flying-missile_djvu, dtype: float64
(Ranges from 0 - 1. Lower score is more similar)
```

Here are the contents of `lccn_sn91069201_1950-02-04_ed-1_seq-7`:
```
THE OFFICIAL HOLY YEAR PRAYER
The prayer composed by Pope Pius XII for the Holy Year
1950, translated into English and printed in convenient leaflet
form (3x5^4 inches) for insertion into missal or prayer book.
Suitable for congregational recitation. With notation of condi
tions for indulgences, and the Imprimatur of His Excellency,
the Most Rev. Archbishop Murray.
Single copies 5 cents.
10 to 99 copies 1 cent each.
100 to 499 copies cent each.
500 or more ife cent each.
WANDERER PRINTING COMPANY
128 East Tenth Street, ST. PAUL 1, MINNESOTA
```

Obviously not a correct match at all, *but* this segment is somewhat simialar to a section of the Pressbook (p4) describing materials that exhibitors can order:

```
SHOW AIDS 


STORY: * storvinec 


" tures (stills and 


Invite to your opening night 














captions) is available for 
newspaper reproduction. If 
your paper will cooperate, 
write Publicity Dept., Room 
901, Columbia Pictures 
Corp., 729 7th Ave., N. Y. 19. 
The material will be mailed 
to the paper and your thea- 
tre will be mentioned. 


STILLS , Available from 


National 
Screen: 1) set of 25 flat stills; 
2) set of 25 uprights; 3) art 
set of 8 (key art from the ads 


and posters); 4) publicity- 


exploitation set (stills used 





in scenes and exploitation). 
```


FYI - the `_` characters can be replaced back with `/` to form URLs to access the page online:

`lccn_sn91069201_1950-02-04_ed-1_seq-7` -> `/lccn/sn91069201/1950/02/04/ed/1/seq/7` -> [https://chroniclingamerica.loc.gov/lccn/sn91069201/1950-02-04/ed-1/seq-7/](https://chroniclingamerica.loc.gov/lccn/sn91069201/1950-02-04/ed-1/seq-7/)


And then the IA identifiers can be converted back into URLs just as easily:

`pressbook-col-the-flying-missile` -> [https://archive.org/details/pressbook-col-the-flying-missile](https://archive.org/details/pressbook-col-the-flying-missile)