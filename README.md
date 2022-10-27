# anxiety_ambiguity_study
This repository contains the data and code (task and analysis) for a study examining how responses to ambiguity correspond to anxiety during the transition to adulthood.

*Corresponding paper.*

**Title: Neural representations of ambiguous affective stimuli and resilience to anxiety in emerging adults.**

**Authors: Natalie Saragosa-Harris, João F. Guassi Moreira, Yael H. Waizman, Anna Sedykin, Jennifer A. Silvers+, and Tara S. Peris+
+Equal author contribution.**


The representational similarity analysis scripts (in scripts/rsa_scripts) use nilearn, a Python package (https://nilearn.github.io/stable/index.html).

If you are getting errors about libraries not loading, you probably have not installed the necessary requirements. To do so, type this: pip install -r requirements.txt
Note: If the virtual environment doesn’t seem to be working, this is how you delete it and create a new one. rm -rf venv module load python/3.7.0 python3.7 -m venv venv/ . venv/bin/activate pip install -r requirements.txt
