# CloseAPIReport

This incomplete script begins by using the Panda package to parse the provided CSV and remove duplicate entries by Contact name. A more refined versions would better handle additional contact methods, though it does normalize naming patterns. 

The next method posts the cleaned CSV file to my Close instance using the close_api library, and the next method queries the Close instance for results created since March of this year. Further work would find the requested values of the report and export them as a CSV using Panda.

dependencies are panda, close_api
