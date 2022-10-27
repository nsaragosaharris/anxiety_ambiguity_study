# anxiety_ambiguity_study
This repository contains the data and code (task and analysis) for a study examining how responses to ambiguity correspond to anxiety during the transition to adulthood.

*Corresponding paper.*

**Title: Neural representations of ambiguous affective stimuli and resilience to anxiety in emerging adults.**

**Authors: Natalie Saragosa-Harris, João F. Guassi Moreira, Yael H. Waizman, Anna Sedykin, Jennifer A. Silvers+, and Tara S. Peris+
+Equal author contribution.**


The stimuli for the fMRI task and post-scan behavioral task (code is located in scripts/task) are from the Racially Diverse Affective Expression (RADIATE) face stimulus set (https://www.sciencedirect.com/science/article/pii/S0165178117321893), an open access dataset available in the supplemental materials for the study.

The representational similarity analysis scripts (in scripts/rsa_scripts) are written in Python 3 use nilearn (https://nilearn.github.io/stable/index.html), a Python library.

If you are getting errors about libraries not loading, you probably have not installed the necessary requirements. To do so, type this: pip install -r requirements.txt
Note: If the virtual environment doesn’t seem to be working, this is how you delete it and create a new one. rm -rf venv module load python/3.7.0 python3.7 -m venv venv/ . venv/bin/activate pip install -r requirements.txt
