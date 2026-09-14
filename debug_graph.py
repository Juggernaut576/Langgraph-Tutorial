from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Literal

class ReviewState(TypedDict):
    review: str
    sentiment: Literal['positive','negative']
    diagnosis: dict
    response: str


def find_sentiment(state:ReviewState):
    return {'sentiment':'positive'}

def check_sentiment(state:ReviewState):
    if state['sentiment']=='positive':
        return 'positive'
    return 'negative'

def positive_response(state:ReviewState):
    return {'response':'ok'}

def run_diagnosis(state:ReviewState):
    return {'diagnosis':{'issue_type':'delivery','tone':'angry','urgency':'high'}}

def negative_response(state:ReviewState):
    return {'response':'sorry'}

graph = StateGraph(ReviewState)
graph.add_node('find_sentiment', find_sentiment)
graph.add_node('run_diagnosis', run_diagnosis)
graph.add_node('negative_response', negative_response)
graph.add_node('positive_response', positive_response)

graph.add_edge(START,'find_sentiment')
graph.add_conditional_edges('find_sentiment', check_sentiment, {'positive':'positive_response','negative':'run_diagnosis'})
graph.add_edge('positive_response',END)
graph.add_edge('run_diagnosis','negative_response')
graph.add_edge('negative_response',END)

workflow = graph.compile()
print('Compiled OK')
initial_state = {'review':'x'}
print(workflow.invoke(initial_state))
