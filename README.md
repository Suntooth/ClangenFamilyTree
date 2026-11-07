# ClangenFamilyTree
Creates a FamilyScript family tree from a Clangen savefile.

Confirmed to work in Python 3.14.6. Your mileage may vary with other versions.
 
## How to use
1. Install Python.
2. Download `familytree.py`.
3. Run `familytree.py`.
4. When it asks for the path to the save, enter it - specifically the path to the folder named after your clan (e.g. `[...]/saves/Kestrel/` rather than `[...]/saves/`).
5. The program will create a file, `[clan name]_familytree.txt`. Import that file into [Family Echo](https://www.familyecho.com/) to view it.

Note that due to the size and relative complexity of clan dynamics, the family tree will probably be quite large and difficult to read. That's just a consequence of how clans work compared to human families, not anything to do with this program. Also note that you will probably want to view the tree in "Multiple" or "Complete" mode, rather than "Partial".

## Future plans
I've been having trouble with Family Echo's API, but if I can get it to work I'd like this program to get a view link from that API, so that the user doesn't have to manually import the tree.
