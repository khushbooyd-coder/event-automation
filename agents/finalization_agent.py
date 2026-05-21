def finalize_best_venue(
    venue_outreach_results
):

    best_option = None

    best_roi_score = 0

    for venue in venue_outreach_results:

        if not venue.get(
            "proposal_received"
        ):
            continue

        # --------------------------------
        # EXTRACT PRICE
        # --------------------------------

        price_text = (
            venue["quoted_price"]
            .replace("$", "")
            .replace(",", "")
        )

        price = int(price_text)

        # --------------------------------
        # ROI SCORING
        # --------------------------------

        roi_score = 10000 / price

        if roi_score > best_roi_score:

            best_roi_score = roi_score

            # --------------------------------
            # SAFE VENUE NAME EXTRACTION
            # --------------------------------

            venue_name = venue.get(
                "venue_name",
                venue.get(
                    "name",
                    "Unknown Venue"
                )
            )

            
            best_option = {

                "venue_name":
                    venue_name,

                "quoted_price":
                    venue["quoted_price"],

                "status":
                    "Venue Finalized",

                "roi_score":
                    round(
                        roi_score,
                        2
                    ),

                "venue_email":
                    venue.get(
                        "venue_email",
                        "events@example.com"
                    ),

                "reason":
                    (
                        "Selected based on "
                        "highest ROI and "
                        "proposal efficiency."
                    )
            }


    return best_option

