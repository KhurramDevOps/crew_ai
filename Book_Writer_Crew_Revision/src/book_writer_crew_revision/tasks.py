from crewai import Task

from crewai_tools import SerperDevTool, ScrapeWebsiteTool

from dotenv import load_dotenv

load_dotenv()

search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()


class BookWriterTask:

    def Outline_Writer_Task(self, agent , topic):
        return Task(
            description =f""" 
            Write a detailed outline for a book on the topic search on the internet fot latest
            and trending topics in the book industry. 

            Paramters:
            -------------
            topic : {topic}
            
            """,
            tools =[search_tool,scrape_tool],
            agent= agent,
            expected_output=""" 

                    A detailed outline for the book in the fromat of the following:
                    Topic: {topic}
                    Outline:
                    - Introduction
                        - Chapter 1 with brief description
                        - Chapter 2 with brief description
                        - Chapter 3 with brief description
                        - Chapter 4 with brief description
                        - Chapter 5 with brief description
                        - Conclusion
                        - References
                    

 """,

        )