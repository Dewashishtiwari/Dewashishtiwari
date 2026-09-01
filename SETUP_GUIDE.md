# Publish Dewashish's GitHub profile

This repository is ready except for the exact GitHub username. GitHub displays a profile README only when the public repository name exactly matches the account username.

## 1. Configure the username

From the repository folder, run:

    python scripts/configure_profile.py --username Dewashishtiwari
    python scripts/validate_profile.py --strict

The first command updates the statistics cards, metrics configuration and profile settings. The second checks that no username placeholder remains and that all local SVG assets are valid.

## 2. Create the special profile repository

On GitHub:

1. Create a **public** repository.
2. Name it exactly <code>Dewashishtiwari</code>.
3. Do not add a README, license or gitignore because they are already included here.
4. From this folder, publish the files:

    git init
    git add .
    git commit -m "feat: launch scientific GitHub profile"
    git branch -M main
    git remote add origin https://github.com/Dewashishtiwari/Dewashishtiwari.git
    git push -u origin main

Visit <code>https://github.com/Dewashishtiwari</code> to see the profile.

## 3. Enable the automated visuals

In the profile repository:

1. Open **Settings → Actions → General**.
2. Under **Workflow permissions**, choose **Read and write permissions**.
3. Save.
4. Open **Actions** and manually run:
   - **Generate contribution snake**
   - **Generate 3D contribution landscape**

The starter panels in the repository will be replaced by live contribution visuals. The write-enabled generators are deliberately manual-only and pinned to immutable action commits; rerun them whenever you want to refresh the visuals.

## 4. Optional rich metrics

The expanded metrics panel is optional because it needs a personal access token to read account-level GitHub activity.

1. Create a fine-grained token with the smallest practical read-only access.
2. Add it at **Settings → Secrets and variables → Actions**.
3. Name the secret <code>METRICS_TOKEN</code>.
4. Run **Generate expanded GitHub metrics** from the Actions tab.

Never place a token directly in a workflow, README or committed configuration file.

## 5. Complete the native GitHub profile

Recommended public settings:

- **Name:** Dewashish Tiwari
- **Bio:** Atmospheric scientist | Air quality, climate extremes & environmental health | WRF-Chem + Earth-system data
- **Company:** Indian Institute of Technology Bombay
- **Location:** Mumbai, India
- **Website:** Google Scholar or a future research portfolio
- **Social link:** LinkedIn
- **Profile photo:** clear, square headshot with a simple background
- **Status:** Open to postdoctoral and research collaborations
- **Social preview:** upload `assets/social-preview.png` in the repository's social preview settings

Also:

- enable the activity overview;
- decide whether to display anonymized private contribution counts;
- verify that the email used for commits is connected to GitHub;
- enable two-factor authentication; and
- pin up to six strong public repositories as they become available.

## 6. Recommended first six pinned repositories

Use the roadmap in [REPOSITORY_ROADMAP.md](REPOSITORY_ROADMAP.md). Each repository should include:

- an informative README with one strong figure;
- an environment file and reproducible example;
- a license and citation instructions;
- sample or synthetic data when original data cannot be redistributed;
- tagged releases; and
- a DOI through Zenodo for stable research software.

## Privacy decisions already applied

The public profile includes one professional contact email. It intentionally excludes phone numbers, home information and referee contact details from the supplied CV.
