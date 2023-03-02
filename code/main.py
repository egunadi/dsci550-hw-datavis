import consolidate_pixstory_data
import scrub_pixstory_data
import sporting_events
import film_festivals
import Hate_Speech
import analyze_sarcasm_data
import analyze_diagnosis_data
import analyze_hobby_data
import depression_anxiety_index

if __name__ == '__main__':
    # 1. extract pixstory data in '../data/pixstory'
    
    # 2. consolidate and scrub pixstory data
    consolidate_pixstory_data.consolidate_pixstory_data()
    consolidate_pixstory_data.convert_csv_to_tsv()
    scrub_pixstory_data.scrub_pixstory_data()
    
    # 3. add features (may need to run one at a time)
    sporting_events.post_event_date_match()
    film_festivals.post_filmfestival_date_match() # may need to run several times
    Hate_Speech.flag_pixstory_hate()
    analyze_sarcasm_data.flag_pixstory_sarc()
    analyze_diagnosis_data.flag_pixstory_dx()
    analyze_hobby_data.joinHobbiesToPix()
    depression_anxiety_index.merge_AD_indexes() # may take close to 3 mins to complete
    