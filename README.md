# Task Scheduler

## Team name: codepyrates

### Team members:
  *  Hamza Ahmad
  *  Mona Salih
  *  Morad Alkhatib
  *  Khaled Alqrainy

## Idea Description:

This program acts as a personal assistant, the user should be able to either add reminders or to select from a list of tasks that can also be scheduled. This programme helps people manage tasks and can operate directly on the system as user command

--- 
## [Domain_Modeling_link](https://drive.google.com/file/d/1myV-2WrUYNV6yJfeshDiKAo6QfwcRDY3/view?usp=sharing)

## User Stories

### 1. Reminders

As a user I want to set reminders so that I don’t miss the tasks I plan to do.

#### Feature Tasks

1. The user can type a message in the reminder which will get shown once the alarm goes off.

    * given [the user set message for reminder]

    * when [user typeds the message]

    * then [message saved]

2. The user can set the time for the alarm.

    * given [the user set alarm for message]

    * when [user choose time to start the task]

    * then [alarm saved]

3. The user can save or cancel the reminder while setting it up..

    * given [user can save/delete reminder]

    * when [user choose to save task/ delete]

    * then [save/delete]


4. The user can dismiss the alarm once it goes off.

    * given [user can dismiss alarm]

    * when [user can close the alarm]

    * then [dismiss alarm(didnt show again)]

5. The user can modify the details of the reminders as long as they are not due yet.

    * given [user can change on reminder details]

    * when [can change time/ task type/ message]

    * then [save new change and show it at due time]

#### Acceptance Tests

1. Ensure that the alarm goes off at the specified time.
2. Ensure that the reminder shows the entered message.
3. Ensure that the alarm is dismissed when the user does so.

### 2. App Grouping

As a user I want to have some apps set up automatically for me so that I can use them directly without the need to open them manually.

#### Feature Tasks

1. The user can select the apps he wants open.

    * given [user can choose apps in schdualer time]

    * when [can choose apps to complet the task]

    * then [app open directly at schdualer time]
    
2. The user can set the time for the apps he selected.

    * given [user can set timer when app will show]

    * when [can choose when he want to see choosen app]

    * then [the app open on specific time]

3. The user can name the app group.

    * given [user can compiend the app in one group and named the group]

    * when [choose the group name]

    * then [the user can see app group he choose before]

4. The user can modify the details of the group.

    * given [user can change group details befor due time]

    * when [update on group details]

    * then [the user can see app group he choose before]


#### Acceptance Tests

1. Ensure that all the selected apps in the group launch the specified time.
2. Ensure that the user can see all the group details.
3. Ensure that the apps do not launch if the user currently uses their device but instead it shows them a notification if he wants to proceed or not.

### 3. Note Taking

As a user I want to add notes and view them.

#### Feature Tasks

1. The user can view the notes he added before.

    * given [user can show the note]

    * when [read the note at due time or when he update the task]

    * then [note appears clearly on a task description]

2. The user can add new notes.

    * given [user can add new note to task discription]

    * when [can update task note]

    * then [saved new adds]

3. The user can modify the title or the content of the notes.

    * given [user can update note detalis such as title and contant]

    * when [can update task details]

    * then [saved new update]

4. The user can mark some notes as important so that they appear on top of other notes in the index.

    * given [user can mark important note]

    * when [choose important note]

    * then [important note will dispaly at the top]

5. The user can search for the note by keyword.

    * given [user can set keyword for note]

    * when [choose keyword]

    * then [all the note connect to keyword will appear on user search]

6. The user can export notes as files of various supported formats.

    * given [user can export note as file]

    * when [export note as file]

    * then [can show note as format file]


#### Acceptance Tests

1. Ensure that the most important notes appear first.
2. Ensure that the user can view and modify notes without any issues.
3. Ensure that searching by keywords returns the note that contains that keyword or part of it.
4. Ensure the exporting notes yields working files.

### 4. Topic Search

As a user I want to search for a topic and see a list of articles from a set of sites so that I can either read them directly , or save them for later in my notes, or set a reminder to read them later.

#### Feature Tasks

1. The user can type the name of the topic and see a list of related articles.
2. The user can select or choose which article to read from the results.
3. The user can save articles in reminders to read them later locally.

#### Acceptance Tests

1. Ensure the searching of a topic shows the user a number of titles for the articles that match.
2. Ensure that the index of the article opens the content of that article in the terminal.
3. Ensure that the article is saved for later if the user chooses to read later.

### 5. Entertainment

As a user  I want something simple to entertain me that does not interfere with my schedule.

#### Feature Tasks

1. The program can predict the time when the user is not busy with anything (idle).
2. The user expects some entertaining activities like playing music or a simple game.
3. The user can dismiss or decline the proposed activity.
4. The user can turn off this feature.

#### Acceptance Test

1. Ensure the program can expect the times when the use is not busy.
2. Ensure the feature gets turned off when the user does so.
3. Ensure the program will offer the user something entertaining or joyful.

