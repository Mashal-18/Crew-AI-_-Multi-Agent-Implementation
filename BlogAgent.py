from crewai import Agent
from Tools import yt_tool

# Create a senior blog content researcher
blog_researcher = Agent(
    role='Blog Researcher from Youtube Videos',
    goal='get the relevant video transcription for the topic {topic} from the provided Yt channel',
    verbose=True,
    memory=True,
    backstory="""You are an expert researcher with a keen eye for detail. 
    Your expertise lies in extracting meaningful information from video content 
    and organizing it in a way that's useful for content creation.""",
    tools=[yt_tool]
)

# Create a blog writer agent (example)
blog_writer = Agent(
    role='Blog Writer',
    goal='write a comprehensive blog post on the topic {topic}',
    verbose=True,
    memory=True,
    backstory="""You are an expert writer with a knack for creating engaging and informative blog posts. 
    Your expertise lies in transforming research into well-written content.""",
    tools=[]
)