class Solution(object):
    def scoreValidator(self, events):
        score = 0
        counter = 0

        for event in events:
            if event.isdigit():
                score += int(event)
            elif event == "W":
                counter += 1
                if counter == 10:
                    break
            else:   # "WD" or "NB"
                score += 1

        return [score, counter]