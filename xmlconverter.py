import io
import os

# SETTINGS
path = r'C:\Users\joost\Downloads\transfer_1082231_files_69f72958\ACAD_whatsapp_manon_20181024\folia'

debugmode = False

# for each file in specified path
for entry in os.scandir(path):

    # if file is of type folia (excluding metadata)
    if entry.path.endswith("folia.xml"):

        print(entry.path)

        # create an txt counterpart to write output to later on
        output_path = entry.path
        output_path = output_path.replace(".folia.xml", ".txt")

        # read actual text
        file_instance = open(entry.path, "r", encoding="cp1252")
        text = file_instance.read()

        # open file
        f = io.open(output_path, "w", encoding="utf-8")

        # we found a hacky solution for a simpler and quicker converter
        actor = text.find("actor=")
        while actor != -1:

            actor = text.find("actor=")

            if actor >= 0:
                # we increment for the letters actor=
                actor_index = actor + 6

                # we find the thing after it (begindatetime)
                after_actor = text.index("begindatetime")

                # we decrement for the space thats between
                after_actor = after_actor - 1

                # now we grab whats in between
                found_actor = text[actor_index:after_actor]

                # next we remove spaces and quotation marks
                found_actor = found_actor.replace(' ', '')
                found_actor = found_actor.replace('"', '')

                # get the corresponding text message
                original_index = text.index("original")

                # increment the index
                original_index = original_index + 10

                # substring
                stringpart = text[original_index:original_index+500]

                if stringpart.find("</t>") == -1:
                    stringpart = text[original_index:original_index+2500]

                if stringpart.find("</t>") == -1:
                    print(stringpart)

                # find the end
                end_index = stringpart.find("</t>") + original_index

                # now we grab whats in between
                found_text = text[original_index:end_index]

                # finally we update the text to filter out the found occurences
                text = text[end_index+10:]

                # DEBUG
                if debugmode == True:
                    print(found_actor + " " + found_text)

                # OUTPUT
                f.write(found_actor + " " + found_text + "\n")
