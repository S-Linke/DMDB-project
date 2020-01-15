
def calculate_ratios(goldstandard, found_duplicates, nonduplicates):
    TP = 0
    FP = 0
    FN = 0
    TN = 0

    print('found duplicates length:',len(found_duplicates))
    print('goldstandard length:',len(goldstandard))

    for i in range(len(found_duplicates)):
        k = 0
        for j in range(len(goldstandard)):
            if found_duplicates.loc[i, "id1"] == goldstandard.loc[j, "id1"]:
                if found_duplicates.loc[i, "id2"] == goldstandard.loc[j, "id2"]:
                    TP += 1
                    k += 1
        if k == 0:
            FP += 1

    for j in range(len(goldstandard)):
        k = 0
        for i in range(len(found_duplicates)):
            if found_duplicates.loc[i, "id1"] == goldstandard.loc[j, "id1"]:
                if found_duplicates.loc[i, "id2"] == goldstandard.loc[j, "id2"]:
                    k += 1
        if k == 0:
            print(j)
            FN += 1

    TN = len(nonduplicates)-FP
    recall = TP / (TP + FN)
    precision = TP / (TP + FP)
    F1 = 2 * (precision * recall) / (precision + recall)
    accuracy = (TP + TN) / (TP + FP + FN + TN)
    FNR = FN / (TP + FN)
    FDR = FP / (TP + FP)


    print('TP =', TP)
    print('TN =', TN)
    print('FP =', FP)
    print('FN =', FN)
    print('Recall =', recall)
    print('Precision =', precision)
    print('F1-Scor e =', F1)
    print('accuracy =', accuracy)
    print('False negative rate =', FNR)
    print('False discovery rate =', FDR)