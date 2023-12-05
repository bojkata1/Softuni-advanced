import unittest
from project.student import Student


class StudentTests(unittest.TestCase):

    def setUp(self):
        self.student_1 = Student("TestName")
        self.student_2 = Student("TestName", {"TestCourse": ["TestNote"]})

    def test_init_without_courses(self):
        self.assertEqual("TestName", self.student_1.name)
        self.assertEqual({}, self.student_1.courses)

    def test_init_with_courses(self):
        self.assertEqual("TestName", self.student_2.name)
        self.assertEqual({"TestCourse": ["TestNote"]}, self.student_2.courses)



    def test_enroll_course_in_courses(self):
        result = self.student_2.enroll("TestCourse", ["note1", "note2", "note3"], add_course_notes="N")
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({"TestCourse": ["TestNote", "note1", "note2", "note3"]}, self.student_2.courses)

        result = self.student_2.enroll("TestCourse", ["note4", "note5", "note6"], add_course_notes="Y")
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({"TestCourse": ["TestNote", "note1", "note2", "note3", "note4", "note5", "note6"]},
                         self.student_2.courses)

    def test_enroll_new_course_and_notes(self):
        result = self.student_1.enroll("TestCourse", ["note1", "note2", "note3"], add_course_notes="Y")
        self.assertTrue("TestCourse" in self.student_1.courses)
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(["note1", "note2", "note3"], self.student_1.courses["TestCourse"])

    def test_enroll_new_course_and_notes_empty_string(self):
        result = self.student_1.enroll("TestCourse", ["note1", "note2", "note3"], add_course_notes="")
        self.assertTrue("TestCourse" in self.student_1.courses)
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(["note1", "note2", "note3"], self.student_1.courses["TestCourse"])

    def test_enroll_new_course_and_no_notes(self):
        result = self.student_1.enroll("TestCourse", ["note1", "note2", "note3"], add_course_notes="N")
        self.assertEqual("Course has been added.", result)
        self.assertTrue("TestCourse" in self.student_1.courses)
        self.assertEqual([], self.student_1.courses["TestCourse"])




    def test_add_notes_successful(self):
        result = self.student_2.add_notes("TestCourse", "note4")
        self.assertEqual({"TestCourse": ["TestNote", "note4"]}, self.student_2.courses)
        self.assertEqual("Notes have been updated", result)

    def test_add_notes_course_not_found_raised(self):
        result = "Cannot add notes. Course not found."
        with self.assertRaises(Exception) as ex:
            self.student_1.add_notes("TestCourse", "note4")
        self.assertEqual(result, str(ex.exception))



    def test_leave_course_successful(self):
        result = self.student_2.leave_course("TestCourse")
        self.assertEqual("Course has been removed", result)
        self.assertNotIn("TestCourse", self.student_2.courses)

    def test_leave_course_course_not_found_raised(self):
        result = "Cannot remove course. Course not found."
        with self.assertRaises(Exception) as ex:
            self.student_1.leave_course("TestCourse")
        self.assertEqual(result, str(ex.exception))


if __name__ == "__main__":
    unittest.main()
