# Many2ManyRelation
A many-to-many relationship exists when a row in one table has many related rows in a second table. Likewise, 
those related rows have many rows in the first table. The following shows
examples of.
1)course can contain many students, and studntcan appear in many
different courses.
2)An employee can work on many projects, and a project can have
many employees working on it.
3)An order can contain many items, and an item can appear in many
different orders.
      Accessing information in tables with a many-to-many relationship is
difficult and time consuming. For efficient processing, you can
convert the many-to-many relationship tables into two one-to-many
relationships by connecting these two tables with a cross-reference
table that contains the related columns.
models.py
---------
class CourseModel(models.Model):
 course_no = models.IntegerField(primary_key=True)
 course_name = models.CharField(max_length=30)
 
class StudentModel(models.Model):
 student_no = models.IntegerField(primary_key=True)
 name = models.CharField(max_length=30)
 contact = models.IntegerField()
 course = models.ManyToManyField(CourseModel)
 
 three tables are created Coursemodel,studentmodel,studentmodel_course.
 studentmodel_course consists of id,studentmodel_id,coursemodel_id.
 
 get the course name for a particular student in templates page.
 {% for studentmodel.objects.all in x.course.all %}
 <h3 style="color: blue">{{ y.course_name }}</h3>
 {% endfor %}
