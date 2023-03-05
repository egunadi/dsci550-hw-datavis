# DSCI550 Team 7 - Homework 1: Analysis of the Newest Social Media Dataset Focused on “Clean” and Less Toxic Social Media

https://github.com/egunadi/dsci550-hw-bigdata

See intro section of our report (worked on by Annie Chang) for overview of project.

## Dependencies

```
name: dsci550
channels:
  - conda-forge
  - defaults
dependencies:
  - alabaster=0.7.12=pyhd3eb1b0_0
  - applaunchservices=0.3.0=py39hecd8cb5_0
  - arrow=1.2.3=py39hecd8cb5_1
  - astroid=2.14.2=py39hecd8cb5_0
  - atomicwrites=1.4.0=py_0
  - attrs=22.1.0=py39hecd8cb5_0
  - autopep8=1.6.0=pyhd3eb1b0_1
  - babel=2.11.0=py39hecd8cb5_0
  - backcall=0.2.0=pyhd3eb1b0_0
  - beautifulsoup4=4.11.1=py39hecd8cb5_0
  - binaryornot=0.4.4=pyhd3eb1b0_1
  - black=22.6.0=py39hecd8cb5_0
  - blas=1.0=mkl
  - bleach=4.1.0=pyhd3eb1b0_0
  - bottleneck=1.3.5=py39h67323c0_0
  - brotlipy=0.7.0=py39h9ed2024_1003
  - ca-certificates=2023.01.10=hecd8cb5_0
  - certifi=2022.12.7=py39hecd8cb5_0
  - cffi=1.15.1=py39hc55c11b_0
  - chardet=4.0.0=py39hecd8cb5_1003
  - click=8.0.4=py39hecd8cb5_0
  - cloudpickle=2.0.0=pyhd3eb1b0_0
  - colorama=0.4.6=py39hecd8cb5_0
  - comm=0.1.2=py39hecd8cb5_0
  - cookiecutter=1.7.3=pyhd3eb1b0_0
  - cryptography=38.0.4=py39hf6deb26_0
  - debugpy=1.5.1=py39he9d5cce_0
  - decorator=5.1.1=pyhd3eb1b0_0
  - defusedxml=0.7.1=pyhd3eb1b0_0
  - diff-match-patch=20200713=pyhd3eb1b0_0
  - dill=0.3.6=py39hecd8cb5_0
  - docstring-to-markdown=0.11=py39hecd8cb5_0
  - docutils=0.18.1=py39hecd8cb5_3
  - entrypoints=0.4=py39hecd8cb5_0
  - flake8=6.0.0=py39hecd8cb5_0
  - flit-core=3.6.0=pyhd3eb1b0_0
  - gettext=0.21.0=h7535e17_0
  - giflib=5.2.1=h6c40b1e_3
  - glib=2.69.1=h8346a28_1
  - gst-plugins-base=1.14.0=h4180768_2
  - gstreamer=1.14.0=h0fc69c2_2
  - icu=58.2=h0a44026_3
  - idna=3.4=py39hecd8cb5_0
  - imagesize=1.4.1=py39hecd8cb5_0
  - importlib-metadata=4.11.3=py39hecd8cb5_0
  - importlib_metadata=4.11.3=hd3eb1b0_0
  - inflection=0.5.1=py39hecd8cb5_0
  - intel-openmp=2021.4.0=hecd8cb5_3538
  - intervaltree=3.1.0=pyhd3eb1b0_0
  - ipykernel=6.19.2=py39h01d92e1_0
  - ipython_genutils=0.2.0=pyhd3eb1b0_1
  - isort=5.9.3=pyhd3eb1b0_0
  - jellyfish=0.9.0=py39hca72f7f_0
  - jinja2=3.1.2=py39hecd8cb5_0
  - jinja2-time=0.2.0=pyhd3eb1b0_3
  - jpeg=9e=hca72f7f_0
  - jsonschema=4.17.3=py39hecd8cb5_0
  - jupyter_client=7.4.9=py39hecd8cb5_0
  - jupyter_core=5.2.0=py39hecd8cb5_0
  - jupyterlab_pygments=0.1.2=py_0
  - keyring=23.4.0=py39hecd8cb5_0
  - krb5=1.19.4=hdba6334_0
  - lazy-object-proxy=1.6.0=py39h9ed2024_0
  - lerc=3.0=he9d5cce_0
  - libclang=12.0.0=default_hbc2896b_2
  - libcxx=14.0.6=h9765a3e_0
  - libdeflate=1.8=h9ed2024_5
  - libedit=3.1.20221030=h6c40b1e_0
  - libffi=3.3=hb1e8313_2
  - libiconv=1.16=hca72f7f_2
  - libllvm12=12.0.0=h9b2ccf5_3
  - libpng=1.6.37=ha441bb4_0
  - libpq=12.9=h1c9f633_3
  - libsodium=1.0.18=h1de35cc_0
  - libspatialindex=1.9.3=h23ab428_0
  - libtiff=4.5.0=hcec6c5f_1
  - libwebp=1.2.4=hf6ce154_1
  - libwebp-base=1.2.4=h6c40b1e_1
  - libxml2=2.9.14=hbf8cd5e_0
  - libxslt=1.1.35=h5b33f42_0
  - llvm-openmp=14.0.6=h0dcd299_0
  - lxml=4.9.1=py39h65b224f_0
  - lz4-c=1.9.4=hcec6c5f_0
  - markupsafe=2.1.1=py39hca72f7f_0
  - matplotlib-inline=0.1.6=py39hecd8cb5_0
  - mccabe=0.7.0=pyhd3eb1b0_0
  - mistune=0.8.4=py39h9ed2024_1000
  - mkl=2021.4.0=hecd8cb5_637
  - mkl-service=2.4.0=py39h9ed2024_0
  - mkl_fft=1.3.1=py39h4ab4a9b_0
  - mkl_random=1.2.2=py39hb2f4e1b_0
  - mypy_extensions=0.4.3=py39hecd8cb5_1
  - nbclient=0.5.13=py39hecd8cb5_0
  - nbconvert=6.5.4=py39hecd8cb5_0
  - nbformat=5.7.0=py39hecd8cb5_0
  - ncurses=6.4=hcec6c5f_0
  - nest-asyncio=1.5.6=py39hecd8cb5_0
  - nspr=4.33=he9d5cce_0
  - nss=3.74=h47edf6a_0
  - numexpr=2.8.4=py39he696674_0
  - numpy=1.23.5=py39he696674_0
  - numpy-base=1.23.5=py39h9cd3388_0
  - numpydoc=1.5.0=py39hecd8cb5_0
  - openssl=1.1.1t=hca72f7f_0
  - packaging=22.0=py39hecd8cb5_0
  - pandas=1.5.2=py39h07fba90_0
  - pandocfilters=1.5.0=pyhd3eb1b0_0
  - parso=0.8.3=pyhd3eb1b0_0
  - pathspec=0.10.3=py39hecd8cb5_0
  - pcre=8.45=h23ab428_0
  - pexpect=4.8.0=pyhd3eb1b0_3
  - pickleshare=0.7.5=pyhd3eb1b0_1003
  - pip=22.3.1=py39hecd8cb5_0
  - platformdirs=2.5.2=py39hecd8cb5_0
  - pluggy=1.0.0=py39hecd8cb5_1
  - ply=3.11=py39hecd8cb5_0
  - poyo=0.5.0=pyhd3eb1b0_0
  - prompt-toolkit=3.0.36=py39hecd8cb5_0
  - psutil=5.9.0=py39hca72f7f_0
  - ptyprocess=0.7.0=pyhd3eb1b0_2
  - pycodestyle=2.10.0=py39hecd8cb5_0
  - pycparser=2.21=pyhd3eb1b0_0
  - pydocstyle=6.3.0=py39hecd8cb5_0
  - pyflakes=3.0.1=py39hecd8cb5_0
  - pylint=2.16.2=py39hecd8cb5_0
  - pylint-venv=2.3.0=py39hecd8cb5_0
  - pyls-spyder=0.4.0=pyhd3eb1b0_0
  - pyobjc-core=8.5=py39hc55c11b_0
  - pyobjc-framework-cocoa=8.5=py39h6c40b1e_1
  - pyobjc-framework-coreservices=8.5=py39hca72f7f_0
  - pyobjc-framework-fsevents=8.5=py39hecd8cb5_0
  - pyopenssl=22.0.0=pyhd3eb1b0_0
  - pyqt=5.15.7=py39he9d5cce_0
  - pyqt5-sip=12.11.0=py39he9d5cce_0
  - pyqtwebengine=5.15.7=py39he9d5cce_0
  - pyrsistent=0.18.0=py39hca72f7f_0
  - pysocks=1.7.1=py39hecd8cb5_0
  - python=3.9.13=hdfd78df_2
  - python-dateutil=2.8.2=pyhd3eb1b0_0
  - python-fastjsonschema=2.16.2=py39hecd8cb5_0
  - python-lsp-black=1.2.1=py39hecd8cb5_0
  - python-lsp-jsonrpc=1.0.0=pyhd3eb1b0_0
  - python-lsp-server=1.7.1=py39hecd8cb5_0
  - python-slugify=5.0.2=pyhd3eb1b0_0
  - python.app=3=py39hca72f7f_0
  - pytoolconfig=1.2.5=py39hecd8cb5_1
  - pytz=2022.7=py39hecd8cb5_0
  - pyyaml=6.0=py39h6c40b1e_1
  - pyzmq=23.2.0=py39he9d5cce_0
  - qdarkstyle=3.0.2=pyhd3eb1b0_0
  - qstylizer=0.2.2=py39hecd8cb5_0
  - qt-main=5.15.2=h719ae48_7
  - qt-webengine=5.15.9=h90a370e_4
  - qtawesome=1.2.2=py39hecd8cb5_0
  - qtconsole=5.4.0=py39hecd8cb5_0
  - qtpy=2.2.0=py39hecd8cb5_0
  - qtwebkit=5.212=h24dc246_4
  - readline=8.2=hca72f7f_0
  - rope=1.7.0=py39hecd8cb5_0
  - rtree=1.0.1=py39hecd8cb5_0
  - setuptools=65.6.3=py39hecd8cb5_0
  - sip=6.6.2=py39he9d5cce_0
  - six=1.16.0=pyhd3eb1b0_1
  - snowballstemmer=2.2.0=pyhd3eb1b0_0
  - sortedcontainers=2.4.0=pyhd3eb1b0_0
  - soupsieve=2.3.2.post1=py39hecd8cb5_0
  - sphinx=5.0.2=py39hecd8cb5_0
  - sphinxcontrib-applehelp=1.0.2=pyhd3eb1b0_0
  - sphinxcontrib-devhelp=1.0.2=pyhd3eb1b0_0
  - sphinxcontrib-htmlhelp=2.0.0=pyhd3eb1b0_0
  - sphinxcontrib-jsmath=1.0.1=pyhd3eb1b0_0
  - sphinxcontrib-qthelp=1.0.3=pyhd3eb1b0_0
  - sphinxcontrib-serializinghtml=1.1.5=pyhd3eb1b0_0
  - spyder=5.4.1=py39hecd8cb5_0
  - spyder-kernels=2.4.1=py39hecd8cb5_0
  - spyder-vim=0.1.0=pyhd8ed1ab_0
  - sqlite=3.40.1=h880c91c_0
  - text-unidecode=1.3=pyhd3eb1b0_0
  - textdistance=4.2.1=pyhd3eb1b0_0
  - three-merge=0.1.1=pyhd3eb1b0_0
  - tinycss2=1.2.1=py39hecd8cb5_0
  - tk=8.6.12=h5d9f67b_0
  - toml=0.10.2=pyhd3eb1b0_0
  - tomli=2.0.1=py39hecd8cb5_0
  - tomlkit=0.11.1=py39hecd8cb5_0
  - tornado=6.2=py39hca72f7f_0
  - typing-extensions=4.4.0=py39hecd8cb5_0
  - typing_extensions=4.4.0=py39hecd8cb5_0
  - tzdata=2022g=h04d1e81_0
  - ujson=5.4.0=py39he9d5cce_0
  - unidecode=1.2.0=pyhd3eb1b0_0
  - urllib3=1.26.14=py39hecd8cb5_0
  - watchdog=2.1.6=py39h999c104_0
  - webencodings=0.5.1=py39hecd8cb5_1
  - whatthepatch=1.0.2=py39hecd8cb5_0
  - wheel=0.38.4=py39hecd8cb5_0
  - wrapt=1.14.1=py39hca72f7f_0
  - wurlitzer=3.0.2=py39hecd8cb5_0
  - xz=5.2.10=h6c40b1e_1
  - yaml=0.2.5=haf1e3a3_0
  - yapf=0.31.0=pyhd3eb1b0_0
  - zeromq=4.3.4=h23ab428_0
  - zipp=3.11.0=py39hecd8cb5_0
  - zlib=1.2.13=h4dc903c_0
  - zstd=1.5.2=hcb37349_0
  - pip:
      - appnope==0.1.3
      - asttokens==2.2.1
      - charset-normalizer==3.0.1
      - executing==1.2.0
      - ipython==8.10.0
      - jedi==0.18.2
      - joblib==1.2.0
      - pure-eval==0.2.2
      - pygments==2.14.0
      - requests==2.28.2
      - scikit-learn==1.2.1
      - scipy==1.10.0
      - sklearn==0.0.post1
      - stack-data==0.6.2
      - threadpoolctl==3.1.0
      - tika==2.6.0
      - traitlets==5.9.0
      - wcwidth==0.2.6
prefix: /Users/egunadi/anaconda3/envs/dsci550
```

## Installation

The environment.yml file in GitHub can be used to recreate our environment.

## Running the project

If downloading from GitHub, the "data/pixstory" folder will be empty due to proprietary concerns. This data should be obtained directly from Dr. Mattmann and extracted into the folder.

Results can be reproduced via "code/main.py", which runs the following functions in order:

### Data Consolidation and Cleaning Functions

- consolidate_pixstory_data.consolidate_pixstory_data()
  - Consolidates all Pixstory files into "data/pixstory/pixstory.csv"
  - Worked on by Eben Gunadi 
- consolidate_pixstory_data.convert_csv_to_tsv()
  - Uses "data/pixstory/pixstory.csv" to create "data/pixstory/pixstory.tsv"
  - Worked on by Eben Gunadi 
- scrub_pixstory_data.scrub_pixstory_data()
  - Uses "data/pixstory/pixstory.csv" to create "data/pixstory/pixstory_clean.csv" (see "Data Cleaning" section of our report for details)
  - Worked on by Eben Gunadi 

### Functions that adds features to the dataset

- sporting_events.post_event_date_match()
  - Uses "data/pixstory/pixstory_clean.csv" to create "data/pixstory/pixstory_sports.csv" (see "Sporting Events" section of our report for details)
  - Worked on by Shih-Min (Julia) Huang
- film_festivals.post_filmfestival_date_match()
  - Uses "data/pixstory/pixstory_sports.csv" to create "data/pixstory/pixstory_film.csv" (see "Film Festivals" section of our report for details)
  - Worked on by Yi Chang
- Hate_Speech.flag_pixstory_hate()
  - Uses "data/pixstory/pixstory_film.csv" to create "data/pixstory/pixstory_hate.csv" (see "Hate Speech Dataset" section of our report for details)
  - Worked on by Annie Chang
- analyze_sarcasm_data.flag_pixstory_sarc()
  - Uses "data/pixstory/pixstory_hate.csv" to create "data/pixstory/pixstory_sarc.csv" (see "Sarcasm Dataset" section of our report for details)
  - Worked on by Eben Gunadi 
- analyze_diagnosis_data.flag_pixstory_dx()
  - Uses "data/pixstory/pixstory_sarc.csv" to create "data/pixstory/pixstory_dx.csv" (see "Diagnosis Dataset" section of our report for details)
  - Worked on by Eben Gunadi 
- analyze_hobby_data.joinHobbiesToPix()
  - Uses "data/pixstory/pixstory_dx.csv" to create "data/pixstory/pixstory_hobby.csv" (see "Hobbies Dataset" section of our report for details)
  - Worked on by Lesly Escobar
- depression_anxiety_index.merge_AD_indexes() 
  - Uses "data/pixstory/pixstory_hobby.csv" to create "data/pixstory/pixstory_adindex.csv" (see "Anxiety and Depression Indexes Dataset" section of our report for details)
  - Worked on by Shih-Min (Julia) Huang

Being the last csv created, "data/pixstory/pixstory_adindex.csv" contains all the features generated in this project.
