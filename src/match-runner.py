from functools import reduce
import json
import riot_api
import database as db

connection = db.get_connection()
collection = db.get_connection_to_collection(connection, "tft01")
number_of_matches_per_player = 10

all_summoner_names = riot_api.get_all_summoner_names_in_league(
    riot_api.Available_tiers.challenger.name)
for summoner_index, summoner_name in enumerate(all_summoner_names):
    matches_for_summoner = riot_api.get_matches_by_summoner_name(
        summoner_name, number_of_matches_per_player)
    for match_index, match in enumerate(matches_for_summoner):
        match_details = riot_api.get_match_details(match)
        db.insert_to_collection_if_not_exists(collection, match_details, True)
        print("match {0} of {1} matches of summoner {2} of {3} summoners.".format(
            (match_index+1), len(matches_for_summoner), (summoner_index+1), len(all_summoner_names)))