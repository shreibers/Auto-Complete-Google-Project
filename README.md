

# Auto-Complete-Google-Project 21-22.07.2020 (As part of Adva bootcamp)

The project returns the best completion options for a given prefix of sentence:
The user starts typing the sentence he's in search for, the program receives the partial sentence that was typed and returns 5 of the best options for completion. In order for the completion options to appear quickly we work in two phases: offline and online.

Offline:
We run offline a program that load the data to an efficient file and  all the possible sentences into another file who behave such a map with keys representing the substring and the value is index in the file of the data. After parsing to a map it will only take the program when its online O(1).

Online:
We receive the substring and access the map we have from the Offline phase with substring being the key. As we said the time complexity is O(1). If there's a hit: The values returned from the map are the completion options for the prefix. If there's a miss: We calculate the best completion by assuming he was one character wrong.

Implementation:
In python.

Special thanks:
bootcamp mentors and google mentors.
