from crewai import Crew, Process
from tasks import research_task, write_task
from agents import news_researcher, writer_agent


crew = Crew(
    agents=[news_researcher, writer_agent],
    tasks=[research_task, write_task],
    process=Process.sequential,
    full_output=True,
)

result = crew.kickoff(inputs={'topic':'AI in Education'})
print(result)
