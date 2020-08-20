# Steps to Make a Bunch of Events for Scholars' Lab Website

1. Create a spreadsheet with the first row containing the following columns in
   this order (and including the colon):

   ``` author: start_date: end_date: start_time: end_time: layout: location: slug: title: content: ```


2. Fill in all the details for your events. Each event should have its own row.

   Note that the slug column will become the name of the file later in the process, and it must start with a letter (ie. don't start the slug with the date).

   The data should be in the following format (not including the column text, so, for example, do not include the text `author = ` just the text `ammon-shepherd`) and DO include the double quotes.

    ```
    author =  ammon-shepherd
    start_date =  2019-10-21
    end_date = 2019-10-21
    start_time = 12:00:00
    end_time = 13:00:00
    layout = events
    location = "Clemons 320"
    slug = workshop-2019-10-21-coding-minecraft-on-raspberry-pi
    title = "Coding Minecraft on the Raspberry Pi"
    ```
3. Create the events in the Library's public events calendar in LibCal. If
   registration is required, copy the registration link and paste it back in to
   the content field in the spreadsheet.
4. Save the spreadsheet as a CSV file to your computer.
    - If saving from Microsoft Excell, make sure the file is in UTF-8 format
      and not "UTF-8 Unicode (with BOM) text, with very long lines". You can
      check the file format by running the `file` command in the terminallike
      so: `file workshops.csv`
    - To convert to just UTF-8, run a command like `dos2unix` like so:
      `dos2unix workshops.csv`
5. Create an empty folder on your computer named `events`.
6. Download the `generate-events.py` script and put it in the same folder as the `events` folder. They should be on the same level. From the command line like so: `python generate-events.py workshops.csv`
7. Add the files to the repo via web browser:
- 7.1 For browser based updating
   - 7.1.1 Log in to [Github.com](https://github.com) and go to this repo page: [https://github.com/scholarslab/scholarslab.org/tree/master/collections/_events ](https://github.com/scholarslab/scholarslab.org/tree/master/collections/_events). Click the `Add file` button and Upload files.
   -  7.1.2 Add a short title that tells about the commit.
   -  7.1.3 Add an optional longer description about the commit.
   -  7.1.4 If you're confident this will not break anything, select ` Commit directly to the master branch.` and press the big green button `Commit changes`.
   -  7.1.5 If you're not sure if this will break the site, or want other people to look it over before committing, select `Create a new branch for this commit
   and start a pull request.`, either keep the default name or add your own,
   then press the big green button `Propose changes`.
- 7.2 For terminal based updating (no pull request option, it updates the live website)
   - 7.2.1 In the cloned repo in your terminal, make sure everything is up to date in the `master` branch. `git pull`
   - 7.2.2 Create a new branch. `git checkout -b events-branch`
   - 7.2.3 Add the files from the `events` folder to the `collections/_events` folder in the repo. Copy and paste using a graphical folder viewer or copy from the command line. `cp path/to/events/*.md path/to/scholarslab.org/collections/_events`
   - 7.2.4 Add the new files to the branch: `git add collections/_events` and commit them: `git commit -m "Adding new events"`
   - 7.2.5 Switch back to the master branch: `git checkout master`
   - 7.2.6 Merge changes into master: `git merge events-branch` and fix any conflicts if any.
   - 7.2.7 Push changes to GitHub: `git push origin master`
8. It will take about 10 minutes for the changes to show up on the website.
