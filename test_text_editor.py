import unittest
from text_editor import TextEditor

class TestTextEditor(unittest.TestCase):
    def test_add(self):
        editor=TextEditor()
        editor.add_char('a')
        editor.add_char('b')
        self.assertEqual(editor.text, "ab")

    def test_deete(self):
        editor=TextEditor()
        editor.add_char('x')
        editor.delete_char()
        self.assertEqual(editor.text, "")

    def test_undo_add(self):
        editor=TextEditor()
        editor.add_char('z')
        editor.undo()
        self.assertEqual(editor.text, "")
        
    def test_undo_delete(self):
        editor=TextEditor()
        editor.add_char('y')
        editor.delete_char()
        editor.undo()
        self.assertEqual(editor.text, "y")

    def test_multiple_undos(self):
        editor=TextEditor()
        editor.add_char('a')
        editor.add_char('b')
        editor.delete_char()
        editor.undo()
        editor.undo()
        self.assertEqual(editor.text, "a")

    def text_undo_empty(self):
        editor=TextEditor()
        editor.undo()