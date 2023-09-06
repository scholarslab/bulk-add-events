# Steps to Make a Bunch of Events for Scholars' Lab Website

1. Create a spreadsheet with the first row containing the following columns in
   this order (and including the colon):

   `author: start_date: end_date: start_time: end_time: layout: location: slug: title: content: image: registration:`

   The image and registration columns are optional


2. Fill in all the details for your events. Each event should have its own row.

   *Note that the `slug` column will become the name of the file later in the
   process, and it must start with a letter (ie. don't start the slug with the
   date).*

   The data in each cell should be in the following format (not including the
   column text, so, for example, do not include the text `author = ` just the
   text `ammon-shepherd`). The image cell should have the name of an image
   file (ex. funny-picture.jpg). You will add the image file to the right
   folder in a later step.

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
   registration is required, copy the registration link and paste it back into
   the registration column in the spreadsheet.

4. Save the spreadsheet as a CSV file to your computer.
    - If saving from Microsoft Excell, make sure the file is in UTF-8 format
      and not "UTF-8 Unicode (with BOM) text, with very long lines". You can
      check the file format by running the `file` command in the terminallike
      so: `file workshops.csv`
    - To convert to just UTF-8, run a command like `dos2unix` like so:
      `dos2unix workshops.csv`

5. Create an empty folder on your computer named `events`.

6. Download the `generate-events.py` script and put it in the same folder where
   you made the `events` folder and put the CSV file. The CSV file, events
   folder, and generate-events.py file should all be in the same folder. 

   If you have images, then open the `generate-events.py` file in a code editor.
   Change the line that looks like this: `IMAGE_FOLDER = "workshops"` Change
   `workshops` to be a descriptive name relating to your events, (ex.
   2020-gis-events).

   If you named the CSV file 'workshops.csv', then execute the script from the
   command line like so: `python generate-events.py workshops.csv`

7. Add the files to the repo via web browser:
- 7.1 For browser based updating
   - 7.1.1 Log in to [Github.com](https://github.com) and go to this repo page:
    [https://github.com/scholarslab/scholarslab.org/tree/master/collections/_events ](https://github.com/scholarslab/scholarslab.org/tree/master/collections/_events).
    Click the `Add file` button and Upload files option. Drag or choose all of
    the `.md` files in the `events` folder.
   - 7.1.2 Add a short title that tells about the commit.
   - 7.1.3 Add an optional longer description about the commit.
   - 7.1.4 If you're confident this will not break anything, select ` Commit
     directly to the master branch.` and press the big green button `Commit
     changes`.
   - 7.1.5 If you're not sure if this will break the site, or want
     other people to look it over before committing, select `Create a new
     branch for this commit and start a pull request.`, either keep the default
     name or add your own, then press the big green button `Propose changes`.
   - 7.1.6 If you have images to upload, browse to this page:
     [https://github.com/scholarslab/scholarslab.org/tree/master/assets/post-media ](https://github.com/scholarslab/scholarslab.org/tree/master/assets/post-media).
     - Click the Add File dropdown, then select 'Create new file'. In the new
       page, type in the name of the image folder you used above in the
       `generate-events.py` file, followed by a forward slash `/` (ex.
       2020-gis-events/). 
     - In the new text field, type `.gitkeep`. This will trick GitHub into making
       a new empty folder. 
     - Then click the big green `Commit new file` button at the bottom of the page.
     - Once more, go to the post-media page: 
       [https://github.com/scholarslab/scholarslab.org/tree/master/assets/post-media ](https://github.com/scholarslab/scholarslab.org/tree/master/assets/post-media).
       Select the folder you just created. 
     - Click the 'Add file' drop down, select the 'Upload files' option, and
     - drag or choose all of the images.
     - Add a title and description and then click the green "Commit changes"
       button.

- 7.2 For terminal based updating (no pull request option, it updates the live
- website)
   - 7.2.1 In the cloned repo in your terminal, make sure everything is up to date in the `master` branch. `git pull`
   - 7.2.2 Create a new branch. `git checkout -b events-branch`
   - 7.2.3 Add the files from the `events` folder to the `collections/_events` folder in the repo. 
     Copy and paste using a graphical folder viewer or copy from the command
     line. `cp path/to/events/*.md path/to/scholarslab.org/collections/_events`
   - 7.2.4 If you have images, create a new folder (named the same as the
     IMAGE_FOLDER from above) in the `assets/post-media/` folder (ex.
     assets/post-media/2020-gis-events). Then copy all of the images into that
     newly created folder.
   - 7.2.5 Add the new files to the branch: `git add collections/_events` and
     `git add assets/post-media/`, and then commit them: `git commit -m "Adding new events"`
   - 7.2.6 Test your changes. Run `bundle exec jekyll serve` and test in the
     browser. You may need to delete everything in the `_site` folder first.
   - 7.2.6 Switch back to the master branch: `git checkout master`
   - 7.2.7 Merge changes into master: `git merge events-branch` and fix conflicts if any.
   - 7.2.8 Push changes to GitHub: `git push origin master`
   - 7.2.9 You can now remove the branch: `git branch -d events-branch`
8. It will take about 10 minutes for the changes to show up on the website.
