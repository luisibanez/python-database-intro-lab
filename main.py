#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from google.appengine.ext import ndb


class Student(ndb.Model):
    print "Making new Student"
    name = ndb.StringProperty(required=True)
    university = ndb.StringProperty(required=True)
    age = ndb.IntegerProperty(required=False)


print "Running code"
student = Student(name="Joseph", university="WashU")
student.put()


class MainHandler(webapp2.RequestHandler):
    def get(self):
        student_query = Student.query()
        student_data = student_query.fetch()
        students_string = ""
        for student in student_data:
            students_string = "{0}{1}:{2}, " .format(students_string, student.name, student.university)
            print students_string
        students_string = students_string[:-2]
        print students_string
        self.response.write('Hello world! ' + students_string)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
