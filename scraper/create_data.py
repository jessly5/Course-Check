
import re
import json
import urllib.request
from bs4 import BeautifulSoup


'''
format example:

}
	"CCT352H5": {
		"courseTitleFull": "CCT352H5F - History and Practice of Design (SH) (SSc)",
		"courseDetails": "This course examines the historical development of communication design from the industrial revolution to the present. The student will focus on the emergence of design practice and theory in changing economic, technological and social contexts. [36L]Prerequisites: CCT204H5",
		"coursePrerequisites": "CCT204H5",
		"tags": [
			"Design"
		]
	}
}

'''


def scrape():
    print('collecting data')
    
    page_url = "https://student.utm.utoronto.ca/timetable/timetable?yos=&subjectarea=4&session=20209&courseCode=&sname=&delivery=&courseTitle="

    page = urllib.request.urlopen(page_url)
    soup = BeautifulSoup(page, 'html.parser')

    course_titles = soup.find_all('h4')
    course_details = soup.find_all('div', attrs={'class': 'infoCourseDetails'})
    course_control = soup.find_all('div', attrs={'class': 'enrollment_control'})

    result = [course_titles, course_details, course_control]
    print('finished collecting data')
    return result


def modify(result):
    data = {}
    course_titles = result[0]
    course_details = result[1]
    course_control = result[2]
    wri_hack = 0
    skip = 0
    ccit_program = 'MA COMM, CULTURE, INFO & TECH'

    print("formatting data\n------")
    
    for i in range (len(course_titles)):
        course_title_full = course_titles[i].text.strip()
        #assumption: course codes are in the standard ABC123 + H/Y + 5 + F/W format
        course_code = course_title_full[0:8]

        #+1 since .find() returns -1 if not found but evaluates to True, and that is not what we contextually interpret it as
        ccit_can_take = True if course_control[i-wri_hack].text.strip().find(ccit_program)+1 or "CCT1" in course_code else False

        if ('WRI' in course_code or (not ccit_can_take)):
            print('skipping course ', i+1, ' of ', len(course_titles), ' because it is WRI or restriction excludes CCIT major')
            skip += 1;
            
            #hard coded workaround for the 2 courses that currently don't have any restrictions
            if ('WRI307H5S' in course_title_full or 'WRI490H5F' in course_title_full):
                wri_hack += 1
            
        else:
            course_detail = course_details[i].text.strip()
            
            course_prerequisites_index = course_detail.find("Prerequisites:")
            if (course_prerequisites_index > -1):
                course_prerequisites = course_detail[course_prerequisites_index+len('Prerequisites:')+1:]
            else:
                course_prerequisites = "None"

            tags = tag(course_title_full, course_detail)
            
            data[course_code] = {'courseTitleFull': course_title_full, 'courseDetails': course_detail, 'coursePrerequisites': course_prerequisites, 'tags': tags}

            print('formatting ', i+1, ' of ', len(course_titles), ' courses')
        
    print("------\nfinished formatting data, skipped ", skip)
    return data


def tag(course_title_full, course_detail):
    regex_tags = ['[Pp]rogram', '[Ss]oftware', '[Dd]esign', '[Ii]nternship', '[Hh]uman', '[Rr]esearch', '[Pp]olit', \
            '[Ee]xperiential', '[Mm]anag', '[Mm]edia', '[Mm]arket', '[Aa]dvertis']
    tags = ['Programming', 'Software', 'Design', 'Internship', 'Human', 'Research', 'Politics', \
            'Experiential', 'Management', 'Media', 'Market', 'Advertising']
    relevant_tags = []
    
    for i in range (len(regex_tags)):
        search_result_title = re.search(regex_tags[i], course_title_full)
        search_result_detail = re.search(regex_tags[i], course_detail)
        if (search_result_title or search_result_detail):
            relevant_tags.append(tags[i])

    relevant_tags = relevant_tags if relevant_tags else "No Tags"
    return relevant_tags


def save(data):
    print("saving json")
    with open ('../data.json', 'w') as output:
        json.dump(data, output)
    print("finished saving json")


def main():
    print('script started')
    result = scrape()
    save(modify(result))
    print('script completed')


main()
