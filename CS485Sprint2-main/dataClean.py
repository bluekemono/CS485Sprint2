import argparse
import operator

import pandas as pd
import numpy as np


def main():
    x = pd.read_csv("billionaires.csv")

    # x = data.to_numpy()
    res = x
    # print(res['company.sector'])
    res['company.sector'] = res['company.sector'].replace(['private equity'], 'finance')
    res['company.sector'] = res['company.sector'].replace(['investment banking'], 'finance')
    res['company.sector'] = res['company.sector'].replace(['investments'], 'finance')
    res['company.sector'] = res['company.sector'].replace(['investment mangagment'], 'finance')
    res['company.sector'] = res['company.sector'].replace(['investment'], 'finance')
    res['company.sector'] = res['company.sector'].replace(['investments'], 'finance')
    res['company.sector'] = res['company.sector'].replace(['money management'], 'finance')
    res['company.sector'] = res['company.sector'].replace(['mutal funds'], 'finance')
    res['company.sector'] = res['company.sector'].replace(['hedge funds'], 'finance')
    res['company.sector'] = res['company.sector'].replace([' Finance'], 'finance')
    res['company.sector'] = res['company.sector'].replace([' finance'], 'finance')
    res['company.sector'] = res['company.sector'].replace(['Banking'], 'finance')
    res['company.sector'] = res['company.sector'].replace(['banking'], 'finance')
    res['company.sector'] = res['company.sector'].replace(['asset management'], 'finance')
    res['company.sector'] = res['company.sector'].replace(['financial services'], 'finance')
    res['company.sector'] = res['company.sector'].replace(['finace'], 'finance')

    res['company.sector'] = res['company.sector'].replace([' technology'], 'software')
    res['company.sector'] = res['company.sector'].replace(['technology'], 'software')
    res['company.sector'] = res['company.sector'].replace([' Software'], 'software')
    res['company.sector'] = res['company.sector'].replace([' software'], 'software')
    res['company.sector'] = res['company.sector'].replace(['GPS technology'], 'software')
    res['company.sector'] = res['company.sector'].replace(['GPS technology'], 'software')
    res['company.sector'] = res['company.sector'].replace(['biotech'], 'software')
    res['company.sector'] = res['company.sector'].replace(['computer services'], 'software')
    res['company.sector'] = res['company.sector'].replace(['computers'], 'software')
    res['company.sector'] = res['company.sector'].replace(['data processing'], 'software')
    res['company.sector'] = res['company.sector'].replace(['data storage'], 'software')
    res['company.sector'] = res['company.sector'].replace(['e-commerce, venture capital'], 'software')
    res['company.sector'] = res['company.sector'].replace(['electronics'], 'software')
    res['company.sector'] = res['company.sector'].replace(['electric motors'], 'software')
    res['company.sector'] = res['company.sector'].replace(['electonics'], 'software')
    res['company.sector'] = res['company.sector'].replace(['laptops'], 'software')
    res['company.sector'] = res['company.sector'].replace(['microchips'], 'software')
    res['company.sector'] = res['company.sector'].replace(['new technology'], 'software')
    res['company.sector'] = res['company.sector'].replace(['video technology'], 'software')
    res['company.sector'] = res['company.sector'].replace(['technology publishing'], 'software')
    res['company.sector'] = res['company.sector'].replace(['technology consulting'], 'software')

    res['company.sector'] = res['company.sector'].replace(['metals'], 'raw materials')
    res['company.sector'] = res['company.sector'].replace(['petrochemicals'], 'raw materials')
    res['company.sector'] = res['company.sector'].replace(['textiles'], 'raw materials')
    res['company.sector'] = res['company.sector'].replace(['metals, paper, cement'], 'raw materials')
    res['company.sector'] = res['company.sector'].replace(['timber'], 'raw materials')
    res['company.sector'] = res['company.sector'].replace(['timber and paper'], 'raw materials')
    res['company.sector'] = res['company.sector'].replace(['natural gas'], 'raw materials')
    res['company.sector'] = res['company.sector'].replace(['oil and gas'], 'raw materials')
    res['company.sector'] = res['company.sector'].replace(['palm oil'], 'raw materials')
    res['company.sector'] = res['company.sector'].replace(['oil'], 'raw materials')
    res['company.sector'] = res['company.sector'].replace(['plastic'], 'raw materials')
    res['company.sector'] = res['company.sector'].replace(['mining'], 'raw materials')

    res['company.sector'] = res['company.sector'].replace(['aluminum'], 'raw materials')
    res['company.sector'] = res['company.sector'].replace(['steel'], 'raw materials')
    res['company.sector'] = res['company.sector'].replace(['coal'], 'raw materials')
    res['company.sector'] = res['company.sector'].replace(['copper'], 'raw materials')
    res['company.sector'] = res['company.sector'].replace(['gas'], 'raw materials')

    res['company.sector'] = res['company.sector'].replace(['telecom'], 'communication')
    res['company.sector'] = res['company.sector'].replace(['media, pipelines'], 'communication')
    res['company.sector'] = res['company.sector'].replace(['telecomm'], 'communication')
    res['company.sector'] = res['company.sector'].replace(['advertising'], 'communication')
    res['company.sector'] = res['company.sector'].replace(['telecommunications'], 'communication')
    res['company.sector'] = res['company.sector'].replace(['internet companies'], 'communication')
    res['company.sector'] = res['company.sector'].replace(['internet'], 'communication')
    res['company.sector'] = res['company.sector'].replace(['internet company'], 'communication')
    res['company.sector'] = res['company.sector'].replace(['media'], 'communication')
    res['company.sector'] = res['company.sector'].replace(['mobile phones'], 'communication')
    res['company.sector'] = res['company.sector'].replace(['mobile app'], 'communication')
    res['company.sector'] = res['company.sector'].replace(['telecom'], 'communication')
    res['company.sector'] = res['company.sector'].replace(['Communications'], 'communication')
    res['company.sector'] = res['company.sector'].replace([' Communications'], 'communication')
    res['company.sector'] = res['company.sector'].replace(['cell phones'], 'communication')

    res['company.sector'] = res['company.sector'].replace(['hotels'], 'real estate')
    res['company.sector'] = res['company.sector'].replace(['shopping centers'], 'real estate')
    res['company.sector'] = res['company.sector'].replace(['casinos'], 'real estate')
    res['company.sector'] = res['company.sector'].replace(['construction/real estate'], 'real estate')

    res['company.sector'] = res['company.sector'].replace(['e-commerce'], 'retail')
    res['company.sector'] = res['company.sector'].replace(['apparel retail'], 'retail')
    res['company.sector'] = res['company.sector'].replace(['home improvement retail'], 'retail')
    res['company.sector'] = res['company.sector'].replace(['fashion retail'], 'retail')
    res['company.sector'] = res['company.sector'].replace(['mail order retail'], 'retail')
    res['company.sector'] = res['company.sector'].replace(['sports retail'], 'retail')
    res['company.sector'] = res['company.sector'].replace(['retail, home appliances'], 'retail')
    res['company.sector'] = res['company.sector'].replace(['shoe retail'], 'retail')
    res['company.sector'] = res['company.sector'].replace([' retail'], 'retail')


    res['company.sector'] = res['company.sector'].replace(['hospitals'], 'medicals')
    res['company.sector'] = res['company.sector'].replace(['medical equipment'], 'medicals')
    res['company.sector'] = res['company.sector'].replace(['healthcare'], 'medicals')
    res['company.sector'] = res['company.sector'].replace(['healthcare management'], 'medicals')
    res['company.sector'] = res['company.sector'].replace(['healthcare'], 'medicals')
    res['company.sector'] = res['company.sector'].replace(['medical devices'], 'medicals')
    res['company.sector'] = res['company.sector'].replace(['medical supplies'], 'medicals')
    res['company.sector'] = res['company.sector'].replace(['medical technology'], 'medicals')
    res['company.sector'] = res['company.sector'].replace(['pharmaceuticals'], 'medicals')

    res['company.sector'] = res['company.sector'].replace(['video games'], 'entertainment')
    res['company.sector'] = res['company.sector'].replace(['movies'], 'entertainment')
    res['company.sector'] = res['company.sector'].replace(['online gaming'], 'entertainment')
    res['company.sector'] = res['company.sector'].replace(['publishing'], 'entertainment')
    res['company.sector'] = res['company.sector'].replace(['gaming'], 'entertainment')

    res['company.sector'] = res['company.sector'].replace(['restaurants'], 'service')
    res['company.sector'] = res['company.sector'].replace(['restaurant'], 'service')
    res['company.sector'] = res['company.sector'].replace(['self-storage'], 'service')
    res['company.sector'] = res['company.sector'].replace(['self storage'], 'service')
    res['company.sector'] = res['company.sector'].replace(['shipping'], 'service')
    res['company.sector'] = res['company.sector'].replace(['supermarkets'], 'service')
    res['company.sector'] = res['company.sector'].replace(['groceries'], 'service')
    res['company.sector'] = res['company.sector'].replace(['hospitality'], 'service')
    res['company.sector'] = res['company.sector'].replace(['food'], 'service')

    X = pd.DataFrame(columns=res.columns)

    for index, row in res.iterrows():
        if row['company.sector'] == "software" \
                or row['company.sector'] == "communication" \
                or row['company.sector'] == "entertainment" \
                or row['company.sector'] == "finance" \
                or row['company.sector'] == "retail" \
                or row['company.sector'] == "real estate" \
                or row['company.sector'] == "medicals" \
                or row['company.sector'] == "service" \
                or row['company.sector'] == "raw materials":
            X.loc[len(X.index)] = row

    res.to_csv('billionaires2.csv')
    X.to_csv('billionaires3.csv')

    column_name = ['communication', 'entertainment', 'finance', 'medicals', 'raw materials', 'real estate', 'retail',
                   'service', 'software']
    Xarr = X.to_numpy()

    # combinedX = pd.DataFrame(columns=column_name)
    combinedXarr = np.zeros((1, 9))
    combinedXarr[0][0] = 0
    combinedXarr[0][1] = 0

    # nineSixXarr = np.zeros((1,9))
    # for i in range(1, len(X)):
    #     # print(Xarr[i][2])
    #     if Xarr[i][2]==1996:
    #         # nineSixXarr = np.ones((1,9))
    #         if "software" in Xarr[i][6] or (not isinstance(Xarr[i][18], float) and "Technology-Computer" in Xarr[i][18]):
    #             nineSixXarr[0][8] += Xarr[i][15]
    #         elif "communication" in Xarr[i][6]:
    #             nineSixXarr[0][0] += Xarr[i][15]
    #         elif "entertainment" in Xarr[i][6]:
    #             nineSixXarr[0][1] += Xarr[i][15]
    #         elif "finance" in Xarr[i][6]:
    #             nineSixXarr[0][2] += Xarr[i][15]
    #         elif "medicals" in Xarr[i][6]:
    #             nineSixXarr[0][3] += Xarr[i][15]
    #         elif "raw materials" in Xarr[i][6]:
    #             nineSixXarr[0][4] += Xarr[i][15]
    #         elif "real estate" in Xarr[i][6]:
    #             nineSixXarr[0][5] += Xarr[i][15]
    #         elif "retail" in Xarr[i][6]:
    #             nineSixXarr[0][6] += Xarr[i][15]
    #         elif "service" in Xarr[i][6]:
    #             nineSixXarr[0][7] += Xarr[i][15]
    # nineSixX = pd.DataFrame(columns=column_name, data=nineSixXarr)
    # # combinedX.to_csv('billionairesCleaned.csv')
    # nineSixX.to_csv('billionaires1996.csv')

    Xarr1996 = np.zeros((1, 9))
    for i in range(1, len(X)):
        # print(Xarr[i][2])
        if Xarr[i][2] == 1996:
            # nineSixXarr = np.ones((1,9))
            if "software" in Xarr[i][6] or (
                    not isinstance(Xarr[i][18], float) and "Technology-Computer" in Xarr[i][18]):
                Xarr1996[0][8] += Xarr[i][15]
            elif "communication" in Xarr[i][6]:
                Xarr1996[0][0] += Xarr[i][15]
            elif "entertainment" in Xarr[i][6]:
                Xarr1996[0][1] += Xarr[i][15]
            elif "finance" in Xarr[i][6]:
                Xarr1996[0][2] += Xarr[i][15]
            elif "medicals" in Xarr[i][6]:
                Xarr1996[0][3] += Xarr[i][15]
            elif "raw materials" in Xarr[i][6]:
                Xarr1996[0][4] += Xarr[i][15]
            elif "real estate" in Xarr[i][6]:
                Xarr1996[0][5] += Xarr[i][15]
            elif "retail" in Xarr[i][6]:
                Xarr1996[0][6] += Xarr[i][15]
            elif "service" in Xarr[i][6]:
                Xarr1996[0][7] += Xarr[i][15]
    X1996 = pd.DataFrame(columns=column_name, data=Xarr1996)
    # combinedX.to_csv('billionairesCleaned.csv')
    X1996.to_csv('billionaires1996.csv')


    Xarr2001 = np.zeros((1, 9))
    for i in range(1, len(X)):
        # print(Xarr[i][2])
        if Xarr[i][2] == 2001:
            # nineSixXarr = np.ones((1,9))
            if "software" in Xarr[i][6] or (
                    not isinstance(Xarr[i][18], float) and "Technology-Computer" in Xarr[i][18]):
                Xarr2001[0][8] += Xarr[i][15]
            elif "communication" in Xarr[i][6]:
                Xarr2001[0][0] += Xarr[i][15]
            elif "entertainment" in Xarr[i][6]:
                Xarr2001[0][1] += Xarr[i][15]
            elif "finance" in Xarr[i][6]:
                Xarr2001[0][2] += Xarr[i][15]
            elif "medicals" in Xarr[i][6]:
                Xarr2001[0][3] += Xarr[i][15]
            elif "raw materials" in Xarr[i][6]:
                Xarr2001[0][4] += Xarr[i][15]
            elif "real estate" in Xarr[i][6]:
                Xarr2001[0][5] += Xarr[i][15]
            elif "retail" in Xarr[i][6]:
                Xarr2001[0][6] += Xarr[i][15]
            elif "service" in Xarr[i][6]:
                Xarr2001[0][7] += Xarr[i][15]
    X2001 = pd.DataFrame(columns=column_name, data=Xarr2001)
    # combinedX.to_csv('billionairesCleaned.csv')
    X2001.to_csv('billionaires2001.csv')


    Xarr2014 = np.zeros((1, 9))
    for i in range(1, len(X)):
        # print(Xarr[i][2])
        if Xarr[i][2] == 2014:
            # nineSixXarr = np.ones((1,9))
            if "software" in Xarr[i][6] or (
                    not isinstance(Xarr[i][18], float) and "Technology-Computer" in Xarr[i][18]):
                Xarr2014[0][8] += Xarr[i][15]
            elif "communication" in Xarr[i][6]:
                Xarr2014[0][0] += Xarr[i][15]
            elif "entertainment" in Xarr[i][6]:
                Xarr2014[0][1] += Xarr[i][15]
            elif "finance" in Xarr[i][6]:
                Xarr2014[0][2] += Xarr[i][15]
            elif "medicals" in Xarr[i][6]:
                Xarr2014[0][3] += Xarr[i][15]
            elif "raw materials" in Xarr[i][6]:
                Xarr2014[0][4] += Xarr[i][15]
            elif "real estate" in Xarr[i][6]:
                Xarr2014[0][5] += Xarr[i][15]
            elif "retail" in Xarr[i][6]:
                Xarr2014[0][6] += Xarr[i][15]
            elif "service" in Xarr[i][6]:
                Xarr2014[0][7] += Xarr[i][15]
    X2014 = pd.DataFrame(columns=column_name, data=Xarr2014)
    # combinedX.to_csv('billionairesCleaned.csv')
    X2014.to_csv('billionaires2014.csv')


    print(combinedXarr)


if __name__ == "__main__":
    main()
