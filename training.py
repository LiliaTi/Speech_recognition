import os
import dialogflow_v2
import json


GOOGLE_APPLICATION_CREDENTIALS = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')

project_id = os.environ.get('PROJECT_ID')


def create_dialogflow_intent(project_id, intent):
    client = dialogflow.IntentsClient()
    parent = client.project_agent_path(project_id)
    response = client.create_intent(parent, intent, language_code='ru')
    return response


def train_dialogflow_agent(project_id):
    client = dialogflow.AgentsClient()
    parent = client.project_path(project_id)
    response = client.train_agent(parent)
    return response


def main():
    with open('questions.json', 'r', encoding='utf-8') as my_file:
        questions = json.load(my_file)

    intents = []
    for key in questions.keys():
        training_phrases = []
        question = questions[key]
        for phrase in question['questions']:
            training_phrases.append({"parts": [{"text": phrase}]})
        intent = {
            "display_name": key,
            "messages": [{
                "text":
                {"text": [question['answer']]}
            }],
            "training_phrases": training_phrases
        }
        intents.append(intent)

    for intent in intents:
        create_dialogflow_intent(project_id, intent)

    train_dialogflow_agent(project_id)


if __name__ == '__main__':
    main()
