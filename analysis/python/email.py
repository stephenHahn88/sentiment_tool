def message(friend):
    return f"Hey {friend}!\n\n" \
           f"" \
           f"I hope you're doing well!\n\n" \
           f"" \
           f"I'm working on a project that involves musical sentiment analysis and I need a bunch of annotated data. " \
           f"So I made a little web app to make it easy: https://music-sentiment-tool.herokuapp.com/\n\n" \
           f"" \
           f"If you have time, would you be able to annotate a bit of music? You don't even have to listen to a " \
           f"whole piece, a few phrases would be helpful! (Though the more, the merrier)\n\n" \
           f"" \
           f"Instructions are at the top of the webpage. If you're ok with it, please put your name in the custom " \
           f"id field next to submit. Just so I know who I should go to in case there's a problem.\n\n" \
           f"" \
           f"Please let me know if you have any questions. I'm happy to Zoom or call as well!\n\n" \
           f"" \
           f"All the best,\n" \
           f"Stephen"

if __name__ == "__main__":
       m = message("Apoorva")
       print(m)