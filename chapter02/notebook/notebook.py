import datetime

last_id = 0


class Note:
    """Represent a not in the notebook"""

    def __init__(self, memo, tags=''):
        self.memo = memo
        self.tags = tags
        self.create_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        """Return true if matches, otherwise false"""
        return filter in self.memo or filter in self.tags


class Notebook:
    """Represent a collection of notes"""

    def __init__(self):
        self.notes = []

    def new_note(self, memo, tags=''):
        """Create a new note and add it to the list"""
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        """Locate the note with the given id"""
        for note in self.notes:
            if note.id == note_id:
                return note
        return None

    def modify_memo(self, note_id, memo):
        """Find the note with the given id and change its name to the given value"""
        self._find_note(note_id).memo = memo

    def modify_tags(self, note_id, tags):
        self._find_note(note_id).tags = tags

    def search(self, filter):
        """Find all notes that match the given filter"""
        return [note for note in self.notes if note.match(filter)]
