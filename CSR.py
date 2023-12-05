from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import ssl
import smtplib
import time
from csv_file import target
from passwd import passwd

sender = 'marketingdepartment.kmcrover@gmail.com'
password = passwd

for i in target:
    em = MIMEMultipart() 

    subject = 'ROVER PROJECT: Regards Sponsorship Funding'
    em['From'] = sender
    em['Subject'] = subject
    context = ssl.create_default_context()

    body = """Dear {},

I hope this email finds you well. My name is Ravikant Verma, and I am writing on behalf of the Robotics Society of Kirori Mal College, Delhi University. As passionate students, we have been actively involved in the development of Robotics Application such as Rovers. Our recent accomplishment includes showcasing our innovative Infinit-Rover 2 in front of Prime Minister Shri Narendra Modi and Education Minister Dharmendra Pradhan during the Valedictory Ceremony of Centenary Celebration of University of Delhi and now we are aiming to move a step ahead and participate in International Rover Competitions with our Upgraded Infinit-Rover 3.

Our Rover Project involves designing and building a cutting-edge rover to compete in international challenges. This initiative not only enhances the skills of our student members but also contributes to the overall advancement of science and technology.

We are reaching out to you because we believe {} shares our commitment to fostering innovation and education. The Rover Project aligns with our mission to push the boundaries of technological advancements and inspire future generations. To achieve our goals, we are seeking financial support in the form of CSR funds from organizations that recognize the value of investing in education and technological innovation.

We understand the importance of a symbiotic relationship, and we are open to discussing customized sponsorship packages that align with your corporate objectives.

If you are interested in supporting our project, we would be grateful to arrange a meeting at your convenience to further discuss the details. We are confident that this partnership will not only contribute to the success of our Rover Project but also showcase your company as a supporter of innovation and education.


Best Regards,

Ravikant Verma
Project Chief
Robotics Society of Kirori Mal College, University of Delhi
+91 788 074 9927
""".format(i.name,i.company)

    em.attach(MIMEText(body, 'plain'))

    
    pdf_filename1 = 'Infinit-Rover 3 Proposal.pdf'
    with open(pdf_filename1, 'rb') as attachment1:
        part1 = MIMEApplication(attachment1.read(), Name='Infinit-Rover 3 Proposal.pdf')
        part1['Content-Disposition'] = 'attachment; filename="Infinit-Rover 3 Proposal.pdf"'
        em.attach(part1)

    
    pdf_filename2 = 'KMC-RoboPhysicists Brochure.pdf'
    with open(pdf_filename2, 'rb') as attachment2:
        part2 = MIMEApplication(attachment2.read(), Name='KMC-RoboPhysicists Brochure.pdf')
        part2['Content-Disposition'] = 'attachment; filename="KMC-RoboPhysicists Brochure.pdf"'
        em.attach(part2)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(sender, password)
            em['To'] = i.mail
            smtp.sendmail(sender, i.mail, em.as_string())
        print(f"Email to {i.mail} sent successfully.")
    except Exception as e:
        print(f"Failed to send email to {i.mail}. Error: {e}")

    time.sleep(1)

print("Email sending process completed.")

