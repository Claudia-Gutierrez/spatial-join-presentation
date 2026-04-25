{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "03c3ad9d",
   "metadata": {},
   "source": [
    "## Spatial Join"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5701b8bb-30eb-4ae7-95f6-3d3034562ec1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import geopandas as gpd\n",
    "import pandas as pd\n",
    "from pathlib import Path"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d36b95b8-c9e2-4d07-b61c-7a826992151f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "EPSG:4326\n",
      "EPSG:4326\n"
     ]
    }
   ],
   "source": [
    "base = Path(r\"C:/Your_path\")\n",
    "\n",
    "boroughs = gpd.read_file(base / \"geodata/GM_lad.gpkg\")\n",
    "stops = gpd.read_file(base / \"geodata/Metrolink_Stops_Functional.json\")\n",
    "\n",
    "print(boroughs.crs)\n",
    "print(stops.crs)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7168a29d-80c3-45f0-840b-2d095b1e58a6",
   "metadata": {},
   "source": [
    "Set Coordinate Reference System to OSGB36 / British National Grid"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "efa9f8f0-f3b0-4a01-823e-00704ecca109",
   "metadata": {},
   "outputs": [],
   "source": [
    "boroughs = boroughs.to_crs(epsg=27700)\n",
    "stops = stops.to_crs(epsg=27700)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "340f2824-b2ea-4979-8e08-8618e5ac8a45",
   "metadata": {},
   "source": [
    "Spatial join: assign each stop to the borough it falls within"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "9bb17404-cfd3-49cc-a70d-b27b1d629528",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>description</th>\n",
       "      <th>type</th>\n",
       "      <th>name</th>\n",
       "      <th>validFrom</th>\n",
       "      <th>currentStatus</th>\n",
       "      <th>comments</th>\n",
       "      <th>stationCode</th>\n",
       "      <th>ticketZone</th>\n",
       "      <th>stroke</th>\n",
       "      <th>geometry</th>\n",
       "      <th>index_right</th>\n",
       "      <th>LAD22CD</th>\n",
       "      <th>LAD22NM</th>\n",
       "      <th>BNG_E</th>\n",
       "      <th>BNG_N</th>\n",
       "      <th>LONG</th>\n",
       "      <th>LAT</th>\n",
       "      <th>GlobalID</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Heaton Park Metrolink stop.</td>\n",
       "      <td>railwayStop</td>\n",
       "      <td>Heaton Park</td>\n",
       "      <td>19920406</td>\n",
       "      <td>functional</td>\n",
       "      <td>NaN</td>\n",
       "      <td>HPK</td>\n",
       "      <td>3</td>\n",
       "      <td>#000000</td>\n",
       "      <td>POINT (382382.361 403792.292)</td>\n",
       "      <td>8</td>\n",
       "      <td>E08000002</td>\n",
       "      <td>Bury</td>\n",
       "      <td>379658</td>\n",
       "      <td>410768</td>\n",
       "      <td>-2.30880</td>\n",
       "      <td>53.59310</td>\n",
       "      <td>528b15a7-dba9-46fb-90c3-61505a610756</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Bowker Vale Metrolink stop.</td>\n",
       "      <td>railwayStop</td>\n",
       "      <td>Bowker Vale</td>\n",
       "      <td>19920406</td>\n",
       "      <td>functional</td>\n",
       "      <td>NaN</td>\n",
       "      <td>BKV</td>\n",
       "      <td>2/3</td>\n",
       "      <td>#000000</td>\n",
       "      <td>POINT (383530.343 403163.727)</td>\n",
       "      <td>9</td>\n",
       "      <td>E08000003</td>\n",
       "      <td>Manchester</td>\n",
       "      <td>384591</td>\n",
       "      <td>397063</td>\n",
       "      <td>-2.23359</td>\n",
       "      <td>53.47009</td>\n",
       "      <td>dcb3ecf1-0228-43d0-b65f-f40a4e801466</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Crumpsall Metrolink stop.</td>\n",
       "      <td>railwayStop</td>\n",
       "      <td>Crumpsall</td>\n",
       "      <td>19920406</td>\n",
       "      <td>functional</td>\n",
       "      <td>NaN</td>\n",
       "      <td>CRP</td>\n",
       "      <td>2</td>\n",
       "      <td>#000000</td>\n",
       "      <td>POINT (384114.233 402316.208)</td>\n",
       "      <td>9</td>\n",
       "      <td>E08000003</td>\n",
       "      <td>Manchester</td>\n",
       "      <td>384591</td>\n",
       "      <td>397063</td>\n",
       "      <td>-2.23359</td>\n",
       "      <td>53.47009</td>\n",
       "      <td>dcb3ecf1-0228-43d0-b65f-f40a4e801466</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Bury Metrolink stop.</td>\n",
       "      <td>railwayStop</td>\n",
       "      <td>Bury</td>\n",
       "      <td>19920406</td>\n",
       "      <td>functional</td>\n",
       "      <td>NaN</td>\n",
       "      <td>BRY</td>\n",
       "      <td>4</td>\n",
       "      <td>#000000</td>\n",
       "      <td>POINT (380431.881 410525.928)</td>\n",
       "      <td>8</td>\n",
       "      <td>E08000002</td>\n",
       "      <td>Bury</td>\n",
       "      <td>379658</td>\n",
       "      <td>410768</td>\n",
       "      <td>-2.30880</td>\n",
       "      <td>53.59310</td>\n",
       "      <td>528b15a7-dba9-46fb-90c3-61505a610756</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Radcliffe Metrolink stop.</td>\n",
       "      <td>railwayStop</td>\n",
       "      <td>Radcliffe</td>\n",
       "      <td>19920406</td>\n",
       "      <td>functional</td>\n",
       "      <td>NaN</td>\n",
       "      <td>RAD</td>\n",
       "      <td>4</td>\n",
       "      <td>#000000</td>\n",
       "      <td>POINT (378833.247 407354.405)</td>\n",
       "      <td>8</td>\n",
       "      <td>E08000002</td>\n",
       "      <td>Bury</td>\n",
       "      <td>379658</td>\n",
       "      <td>410768</td>\n",
       "      <td>-2.30880</td>\n",
       "      <td>53.59310</td>\n",
       "      <td>528b15a7-dba9-46fb-90c3-61505a610756</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   description         type         name validFrom  \\\n",
       "0  Heaton Park Metrolink stop.  railwayStop  Heaton Park  19920406   \n",
       "1  Bowker Vale Metrolink stop.  railwayStop  Bowker Vale  19920406   \n",
       "2    Crumpsall Metrolink stop.  railwayStop    Crumpsall  19920406   \n",
       "3         Bury Metrolink stop.  railwayStop         Bury  19920406   \n",
       "4    Radcliffe Metrolink stop.  railwayStop    Radcliffe  19920406   \n",
       "\n",
       "  currentStatus comments stationCode ticketZone   stroke  \\\n",
       "0    functional      NaN         HPK          3  #000000   \n",
       "1    functional      NaN         BKV        2/3  #000000   \n",
       "2    functional      NaN         CRP          2  #000000   \n",
       "3    functional      NaN         BRY          4  #000000   \n",
       "4    functional      NaN         RAD          4  #000000   \n",
       "\n",
       "                        geometry  index_right    LAD22CD     LAD22NM   BNG_E  \\\n",
       "0  POINT (382382.361 403792.292)            8  E08000002        Bury  379658   \n",
       "1  POINT (383530.343 403163.727)            9  E08000003  Manchester  384591   \n",
       "2  POINT (384114.233 402316.208)            9  E08000003  Manchester  384591   \n",
       "3  POINT (380431.881 410525.928)            8  E08000002        Bury  379658   \n",
       "4  POINT (378833.247 407354.405)            8  E08000002        Bury  379658   \n",
       "\n",
       "    BNG_N     LONG       LAT                              GlobalID  \n",
       "0  410768 -2.30880  53.59310  528b15a7-dba9-46fb-90c3-61505a610756  \n",
       "1  397063 -2.23359  53.47009  dcb3ecf1-0228-43d0-b65f-f40a4e801466  \n",
       "2  397063 -2.23359  53.47009  dcb3ecf1-0228-43d0-b65f-f40a4e801466  \n",
       "3  410768 -2.30880  53.59310  528b15a7-dba9-46fb-90c3-61505a610756  \n",
       "4  410768 -2.30880  53.59310  528b15a7-dba9-46fb-90c3-61505a610756  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "stops_in_borough = gpd.sjoin(\n",
    "    stops,\n",
    "    boroughs,\n",
    "    how=\"inner\",\n",
    "    predicate=\"within\"\n",
    ")\n",
    "\n",
    "stops_in_borough.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e6a5fc4f-7e04-42b6-87dd-da9c9c85643d",
   "metadata": {},
   "source": [
    "Count tram stops per borough"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "4d975973-d7ed-45a5-b0bb-5dea80691cf3",
   "metadata": {},
   "outputs": [],
   "source": [
    "borough_counts = (\n",
    "    stops_in_borough\n",
    "    .groupby(\"LAD22NM\")\n",
    "    .size()\n",
    "    .reset_index(name=\"n_stops\")\n",
    "    .sort_values(\"n_stops\", ascending=False)\n",
    ")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0ccc1f04-7b6b-47a0-b04b-52e2d1eaea6c",
   "metadata": {},
   "source": [
    "Boroughs not served by the tram network"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "1568a093-0e17-471a-a0a1-935e5e94ded5",
   "metadata": {},
   "outputs": [],
   "source": [
    "not_served = (\n",
    "    boroughs[[\"LAD22NM\"]]\n",
    "    .merge(\n",
    "        stops_in_borough[[\"LAD22NM\"]].drop_duplicates(),\n",
    "        on=\"LAD22NM\",\n",
    "        how=\"left\",\n",
    "        indicator=True\n",
    "    )\n",
    "    .query('_merge == \"left_only\"')\n",
    "    [[\"LAD22NM\"]]\n",
    ")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5755b3cb-1006-40b1-ab83-2988a28ce806",
   "metadata": {},
   "source": [
    "Inspect outputs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "8eb663ff-e402-42c6-b58b-d1c4794fe7b5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Stops joined to boroughs:\n",
      "          name stationCode     LAD22NM\n",
      "0  Heaton Park         HPK        Bury\n",
      "1  Bowker Vale         BKV  Manchester\n",
      "2    Crumpsall         CRP  Manchester\n",
      "3         Bury         BRY        Bury\n",
      "4    Radcliffe         RAD        Bury\n",
      "\n",
      "Stops per borough:\n",
      "      LAD22NM  n_stops\n",
      "1  Manchester       42\n",
      "6    Trafford       18\n",
      "2      Oldham       10\n",
      "4     Salford       10\n",
      "5    Tameside        7\n",
      "0        Bury        6\n",
      "3    Rochdale        6\n",
      "\n",
      "Boroughs not served:\n",
      "                  LAD22NM\n",
      "0              Warrington\n",
      "1   Blackburn with Darwen\n",
      "2           Cheshire East\n",
      "3               High Peak\n",
      "4                 Chorley\n",
      "5              Rossendale\n",
      "6         West Lancashire\n",
      "7                  Bolton\n",
      "13              Stockport\n",
      "16                  Wigan\n",
      "17             St. Helens\n",
      "18             Calderdale\n",
      "19               Kirklees\n"
     ]
    }
   ],
   "source": [
    "print(\"\\nStops joined to boroughs:\")\n",
    "print(stops_in_borough[[\"name\", \"stationCode\", \"LAD22NM\"]].head())\n",
    "\n",
    "print(\"\\nStops per borough:\")\n",
    "print(borough_counts)\n",
    "\n",
    "print(\"\\nBoroughs not served:\")\n",
    "print(not_served)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f64b1a8f-2515-4b90-a90f-84721a5cfbdc",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.16"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
