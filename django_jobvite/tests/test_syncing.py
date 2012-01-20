from mock import Mock
import test_utils

from django_jobvite.management.commands import syncjobvite
from django_jobvite.models import Category, Position

one_position = """<result>
<job>
  <id>oWqcfdsa</id>
  <title>Software Engineer</title>
  <requisitionid>1229</requisitionid>
  <category>Engineering</category>
  <jobtype>Full-Time</jobtype>
  <location>Mountain View, CA</location>
  <date>2/21/2011</date>
  <detail-url>http://example.com/job</detail-url>
  <apply-url>http://example.com/job</apply-url>
  <description>I am a job<![CDATA[<br><script>alert('I am bad');</script>]]></description>
  <briefdescription>...</briefdescription>
</job>
</result>"""

two_positions = """<result>
<job>
  <id>oWqcfdsa</id>
  <title>Software Engineer</title>
  <requisitionid>1229</requisitionid>
  <category>Engineering</category>
  <jobtype>Full-Time</jobtype>
  <location>Mountain View, CA</location>
  <date>2/21/2011</date>
  <detail-url>http://example.com/job</detail-url>
  <apply-url>http://example.com/job</apply-url>
  <description>I am job</description>
  <briefdescription>...</briefdescription>
</job>
<job>
  <id>fcOwxed</id>
  <title>Software Engineer</title>
  <requisitionid>1229</requisitionid>
  <category>Engineering</category>
  <jobtype>Full-Time</jobtype>
  <location>Mountain View, CA</location>
  <date>2/21/2011</date>
  <detail-url>http://example.com/job</detail-url>
  <apply-url>http://example.com/job</apply-url>
  <description>I am job</description>
  <briefdescription>...</briefdescription>
</job>
</result>"""

updated = """<result>
<job>
  <id>oWqcfdsa</id>
  <title>Software Developer</title>
  <requisitionid>1229</requisitionid>
  <category>Engineering</category>
  <jobtype>Full-Time</jobtype>
  <location>Mountain View, CA</location>
  <date>2/21/2011</date>
  <detail-url>http://example.com/job</detail-url>
  <apply-url>http://example.com/job</apply-url>
  <description>I am job</description>
  <briefdescription>...</briefdescription>
</job>
<job>
  <id>fcOwxed</id>
  <title>Software Developer</title>
  <requisitionid>1229</requisitionid>
  <category>Engineering</category>
  <jobtype>Full-Time</jobtype>
  <location>Mountain View, CA</location>
  <date>2/21/2011</date>
  <detail-url>http://example.com/job</detail-url>
  <apply-url>http://example.com/job</apply-url>
  <description>I am job</description>
  <briefdescription>...</briefdescription>
</job>
</result>"""

empty = """<result></result>"""


class SyncTests(test_utils.TestCase):
    def setUp(self):
        mocked_xml_func = Mock()
        mocked_xml_func.return_value = one_position
        self.command = syncjobvite.Command()
        self.command._get_jobvite_xml = mocked_xml_func

    def _assert_count(self, xml, expected):
        """
        Run the sync with the provided xml and assert that the expected
        number of ``Position`` models exist afterwards.
        """
        self.command._get_jobvite_xml.return_value = xml
        self.command.handle()
        assert Position.objects.count() == expected

    def test_adding_new(self):
        """Test that adding one position works."""
        assert Position.objects.count() == 0
        self._assert_count(one_position, 1)

    def test_description_safe(self):
        """Test that bad tags are stripped."""
        self.command.handle()
        assert Position.objects.all()[0].description == "I am a job<br>alert('I am bad');"

    def test_empty_xml(self):
        """Test that handling an empty xml doc does not delete db records."""
        self._assert_count(one_position, 1)
        self._assert_count(empty, 1)

    def test_removing(self):
        """Test that removing one position works."""
        self._assert_count(two_positions, 2)
        self._assert_count(one_position, 1)

    def test_empty_category(self):
        """Test that a category with no positions is removed."""
        assert not Category.objects.exists()

    def test_updating(self):
        """Test that updating fields in existing positions works."""
        self._assert_count(two_positions, 2)
        positions = Position.objects.all()
        for position in positions:
            assert position.title == 'Software Engineer'
        self._assert_count(updated, 2)
        positions = Position.objects.all()
        for position in positions:
            assert position.title == 'Software Developer'
