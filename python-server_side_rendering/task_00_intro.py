def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template string
    and a list of attendees.

    Args:
        template (str): The invitation template with placeholders.
        attendees (list): A list of dictionaries with attendee data.

    Returns:
        None
    """

    # Vérification des types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(x, dict) for x in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Vérification du contenu vide
    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Traitement de chaque invité
    for index, attendee in enumerate(attendees, start=1):
        text = template
        text = text.replace("{name}", attendee.get("name", "N/A"))
        text = text.replace("{event_title}", attendee.get("event_title", "N/A"))
        text = text.replace("{event_date}", attendee.get("event_date", "N/A"))
        text = text.replace("{event_location}", attendee.get("event_location", "N/A"))

        filename = f"output_{index}.txt"
        with open(filename, "w") as file:
            file.write(text)
