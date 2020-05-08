
import json
import urllib.request
from bs4 import BeautifulSoup


'''
format example:
{
    'CSC148H5': {
        'courseTitleFull': 'CSC148 Introduction to Computer Science',
        'courseDetails': 'First year computer science',
        'coursePrerequisites': [
                'CSC108H5'
        ],
        'tags': 'programming'
    }
}
'''


def scrape():
    print('collecting data')
    
    page_url = "https://student.utm.utoronto.ca/timetable/timetable?yos=&subjectarea=4&session=20199&courseCode=&sname=&delivery=&courseTitle="

    page = urllib.request.urlopen(page_url)
    soup = BeautifulSoup(page, 'html.parser')

    course_titles = soup.find_all('h4')
    course_details = soup.find_all('div', attrs={'class': 'infoCourseDetails'})

    result = [course_titles, course_details]
    print('finished collecting data')
    return result


def modify(result):
    data = {}
    course_titles = result[0]
    course_details = result[1]
    skip = 0

    print("formatting data\n------")
    
    for i in range (len(course_titles)):
        course_title_full = course_titles[i].text.strip()
        #assumption: course codes are in the standard ABC123 + H/Y + 5 + F/W format
        course_code = course_title_full[0:8]

        if ('MGD' in course_code or 'WRI' in course_code):
            print('skipping course ', i+1, ' of ', len(course_titles), ' because it is MGD/WRI')
            skip += 1;
            
        else:
            course_detail = course_details[i].text.strip()
            
            course_prerequisites_index = course_detail.find("Prerequisites:")
            if (course_prerequisites_index > -1):
                course_prerequisites = course_detail[course_prerequisites_index+len('Prerequisites:')+1:]
            else:
                course_prerequisites = "None"

            tags = tag(course_detail)
            
            data[course_code] = {'courseTitleFull': course_title_full, 'courseDetails': course_detail, 'coursePrerequisites': course_prerequisites, 'tags': tags}

            print('formatting ', i+1, ' of ', len(course_titles), ' courses')
        
    print("------\nfinished formatting data, skipped ", skip)
    return data


def tag(course_detail):
    tags = ['coding', 'software', 'design', 'experience', 'perception', 'research', 'political', 'ethics', 'managing', 'media', 'mass', 'advertising']
    relevant_tags = []
    
    for t in tags:
        if t in course_detail:
            relevant_tags.append(t)
    
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
