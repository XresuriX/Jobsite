import pytest
from jobs.models import Job
from .factories import JobsFactory

""""""
def test_new_job_entry(db, jobs_factory):
    job = jobs_factory.create()
    print(job)

    # Retrieve the job from the database using its primary key
    saved_job = Job.objects.get(pk=job.pk)
    #print(saved_job.employer_name)
    
    # Perform assertions to ensure the data was saved correctly
    assert saved_job.job_title == job.job_title
    assert saved_job.job_publisher == job.job_publisher
    assert saved_job.job_description == job.job_description
    assert saved_job.job_max_salary == job.job_max_salary
    assert saved_job.job_country == job.job_country
    assert saved_job.job_posted_at_datetime_utc == job.job_posted_at_datetime_utc
    assert saved_job.job_is_remote == job.job_is_remote


    # Optionally, you can check the count of jobs in the database
    assert Job.objects.count() == 1


# test created to check if data would be saved in database correctly
@pytest.mark.parametrize(
    "attributes",
    [
        {
            "employer_name": "Charles Schwab",
            "employer_logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Charles_Schwab_Corporation_logo.svg/1200px-Charles_Schwab_Corporation_logo.svg.png",
            "employer_website": "http://www.schwab.com",
            "employer_company_type": "Finance",
            "job_publisher": "Schwab Jobs",
            "job_id": "G6qYxpAYyVsAAAAAAAAAAA==",
            "job_employment_type": "FULLTIME",
            "job_title": "Software Web Developer",
            "job_apply_link": "https://www.schwabjobs.com/job/austin/software-web-developer/33727/48110146896",
            "job_apply_is_direct": "False",
            "job_description": "Your Opportunity We help our clients plan for their future and they are passionate about the tools and experiences we provide. We collaborate with user experience and design, business and technology partners across the enterprise to build software experiences our users’ are passionate about. What you are good at Website and Electronic Communications Email, Push, SMS, etc Templates designing, building, or maintaining. Using scripting or authoring languages, management tools, content creation tools, applications and digital media. Conferring with teams in resolving conflicts, prioritizing needs, developing content criteria, or choosing solutions. Directing or performing Website/Electronic Communications updates. Developing or validating test routines and schedules in ensuring that test cases mimic external interfaces and address all browser and device types. Editing, writing, or designing Website content, and directing team members who produce content. Maintaining an understanding of the latest Web applications and programming practices through education, studying, and participating in conferences, workshops, and groups. Identifying problems uncovered by customer feedback and testing and correcting or referring problems to appropriate personnel for correction. Evaluating code in ensuring that it meets industry standards, is valid, is properly structured, and is compatible with browsers, devices, or operating systems; and Determining user needs by analyzing technical requirements. What you have Job Requirements: Bachelor’s degree or foreign degree equivalent in Computer Science, Engineering or related field and five 5 years of experience in the job offered or related role. Skills: Experience and/or education must include: Experience in programming applications using HTML, JavaScript, CSS, Angular/React Js, XML and Json.; SQL/No-SQL databases; Experience working with the continuous integration and continuous deployment CI/CD pipelines; Experience in programming applications using Java/J2EE; Understanding of software quality assurance principles; Experience working in Agile teams. Charles Schwab & Company, Inc. seeks Software Web Developer in Austin, TX.",
            "job_is_remote": "False",
            "job_posted_at_datetime_utc": "2023-04-29T00:00:00.000Z",
            "job_city": "Austin",
            "job_state": "Tx",
            "job_country": "US",
            "job_benefits": "null",
            "job_google_link": "https://www.google.com/search?gl=us&hl=en&rciv=jb&q=web+developer+in+texas+usa&start=0&ibp=htl;jobs#fpstate=tldetail&htivrt=jobs&htiq=web+developer+in+texas+usa&htidocid=G6qYxpAYyVsAAAAAAAAAAA%3D%3D",
            "job_offer_expiration_datetime_utc": "2023-05-29T00:00:00.000Z",
            "job_required_experience": "{no_experience_required:false, required_experience_in_months:60, experience_mentioned:true, experience_preferred:false}",
            "job_required_skills": "null",
            "job_required_education": "{postgraduate_degree:false, professional_certification:false, high_school:false, associates_degree:false, bachelors_degree:false, degree_mentioned:true, degree_preferred:false, professional_certification_mentioned:false, job_experience_in_place_of_education:false}",
            "job_experience_in_place_of_education": "False",
            "job_min_salary": "100000",
            "job_max_salary": "100000",
            "job_salary_currency": "null",
            "job_salary_period": "null",
            "job_highlights": "{'Qualifications':[0:'Job Requirements: Bachelor’s degree or foreign degree equivalent in Computer Science, Engineering or related field and five (5) years of experience in the job offered or related role', 1:'Skills: Experience and/or education must include: Experience in programming applications using HTML, JavaScript, CSS, Angular/React Js, XML and Json.; SQL/No-SQL databases; Experience working with the continuous integration and continuous deployment (CI/CD) pipelines; Experience in programming applications using Java/J2EE; Understanding of software quality assurance principles; Experience working in Agile teams'], 'Responsibilities':[0:'Directing or performing Website/Electronic Communications updates', 1:'Developing or validating test routines and schedules in ensuring that test cases mimic external interfaces and address all browser and device types', 2:'Editing, writing, or designing Website content, and directing team members who produce content', 3:'Maintaining an understanding of the latest Web applications and programming practices through education, studying, and participating in conferences, workshops, and groups', 4:'Identifying problems uncovered by customer feedback and testing and correcting or referring problems to appropriate personnel for correction', 5:'Evaluating code in ensuring that it meets industry standards, is valid, is properly structured, and is compatible with browsers, devices, or operating systems; and Determining user needs by analyzing technical requirements']}",
            "job_posting_language": "en",
        },
        {
            "employer_name": "Charles Schwab",
            "employer_logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Charles_Schwab_Corporation_logo.svg/1200px-Charles_Schwab_Corporation_logo.svg.png",
            "employer_website": "http://www.schwab.com",
            "employer_company_type": "Finance",
            "job_publisher": "Schwab Jobs",
            "job_id": "G6qYxpAYyVsAAAAAAAAAAA==",
            "job_employment_type": "FULLTIME",
            "job_title": "Software Web Developer",
            "job_apply_link": "https://www.schwabjobs.com/job/austin/software-web-developer/33727/48110146896",
            "job_apply_is_direct": "False",
            "job_description": "null",
            "job_is_remote": "False",
            "job_posted_at_datetime_utc": "2023-04-29T00:00:00.000Z",
            "job_city": "Austin",
            "job_state": "Tx",
            "job_country": "US",
            "job_benefits": "null",
            "job_google_link": "https://www.google.com/search?gl=us&hl=en&rciv=jb&q=web+developer+in+texas+usa&start=0&ibp=htl;jobs#fpstate=tldetail&htivrt=jobs&htiq=web+developer+in+texas+usa&htidocid=G6qYxpAYyVsAAAAAAAAAAA%3D%3D",
            "job_offer_expiration_datetime_utc": "2023-05-29T00:00:00.000Z",
            "job_required_experience": "{no_experience_required:false, required_experience_in_months:60, experience_mentioned:true, experience_preferred:false}",
            "job_required_skills": "null",
            "job_required_education": "{postgraduate_degree:false, professional_certification:false, high_school:false, associates_degree:false, bachelors_degree:false, degree_mentioned:true, degree_preferred:false, professional_certification_mentioned:false, job_experience_in_place_of_education:false}",
            "job_experience_in_place_of_education": "False",
            "job_min_salary": "100000",
            "job_max_salary": "100000",
            "job_salary_currency": "null",
            "job_salary_period": "null",
            "job_highlights": "null",
            "job_posting_language": "en",
        },
        {
            "employer_name": "null",
            "employer_logo": "null",
            "employer_website": "null",
            "employer_company_type": "null",
            "job_publisher": "",
            "job_id": "",
            "job_employment_type": "FULLTIME",
            "job_title": "Software Web Developer",
            "job_apply_link": "null",
            "job_apply_is_direct": "False",
            "job_description": "null",
            "job_is_remote": "False",
            "job_posted_at_datetime_utc": "2023-04-29T00:00:00.000Z",
            "job_city": "Austin",
            "job_state": "Tx",
            "job_country": "US",
            "job_benefits": "null",
            "job_google_link": "null",
            "job_offer_expiration_datetime_utc": "2023-05-29T00:00:00.000Z",
            "job_required_experience": "null",
            "job_required_skills": "null",
            "job_required_education": "null",
            "job_experience_in_place_of_education": "False",
            "job_min_salary": '100000100000',
            "job_max_salary": "100000",
            "job_salary_currency": "null",
            "job_salary_period": "null",
            "job_highlights": "null",
            "job_posting_language": "en",
        },
    ],
)
def test_create_job_with_specific_attributes1(db, attributes):
    # Create a job instance with specific attributes using the factory
    job = JobsFactory(**attributes)
    print(job)
    assert isinstance(job, Job)
