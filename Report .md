# **Authors**

Logy Khaled (@Logy), Alaa Hewela (@Alaa253), Tawfek Ahmed Tawfek (@Tawfekahmed25), Rahma mamdouh Mohammed (@Rahmamam2000), Malak Abdelfattah Soula (@Malak), Zeyad Ashraf (@Zashraf03), Nourhan Mahmoud (@NourhanM1) , Mohammed Dahab (@mdahab7)

# **GithubRepository**

[Repository_Stage_4_task](https://github.com/MohammadDahab/HachBio_stage_4_task)

[R source code](https://github.com/MohammadDahab/HachBio_stage_4_task/blob/main/Code%20.R)

[Python source code](https://github.com/MohammadDahab/HachBio_stage_4_task/blob/main/HackBio_stage_4_ML.py)
# **Introduction**

Gliomas are brain tumors with significant heterogeneity, where mutations in the IDH (Isocitrate Dehydrogenase) gene serve as key biomarkers for prognosis and treatment. IDH mutant and wildtype statuses classify gliomas and predict patient outcomes. The study of gene expression data enhances the understanding of molecular differences.

# **Dataset and Preprocessing**

We used gene expression data from the TCGA-LGG cohort, downloaded via TCGABiolinks, and matched with IDH status. Preprocessing involved removing samples with missing IDH status and filtering genes with over 25 zero values. Data normalization ensured consistency for analysis.

# **Results**

Differential expression analysis was conducted using DESeq2 to identify differentially expressed genes between IDH wildtype and mutant gliomas based on an adjusted p-value \< 0.05 and |log2FoldChange| \> 1\. 

The MA plot visualizes the log fold change versus mean normalized counts. Significant outliers indicate potential biomarkers.

![IMG-20241004-WA0030](https://github.com/user-attachments/assets/de7240a3-3a24-455d-9364-32807203641b)

# **Comparison with Target Paper**

Our findings supported the original study’s clustering based on IDH status. However, updated gene expression data suggests that additional clusters may be necessary to uncover more molecular subtypes beyond the six clusters.

# **Machine Learning Approach for Gene Expression Clustering Using K-Means**
We performed K-Means clustering on a gene expression dataset **as the same data used in the paper** .Our goal is to identify distinct clusters within the gene expression data, which can reveal important biological insights.

The gene expression data was initially normalized using `StandardScaler` This step ensures that all features are on the same scale, which is crucial for the 
K-Means algorithm to perform effectively. 

Using K-Means with six clusters, we identified distinct clusters. The clustering performance was evaluated using the `Silhouette Score`, a measure of how similar samples in the same cluster are compared to those in other clusters. We achieved an impressive Silhouette Score of 84.03%, indicating that the clusters were well-formed and separated.

### **Visualization**
To visualize our clustering results ,we plotted the clusters using the first two features of the gene expression data. This allowed us to retain the variance in the dataset while exploring the relationships between samples. The plot showed clear groupings of the gene expression data, with some outliers that could suggest biological variability or noise.

![Figure 2024-10-09 212710](https://github.com/user-attachments/assets/25ae8153-c30d-4331-8b7a-15bad6d2d6cd)

# **Conclusion**

The analysis confirms IDH status is crucial in glioma classification using gene expression data. It suggests new glioma subtypes, encouraging further research into biomarkers and refined treatment strategies.

**Increasing the number of clusters uncovers biologically distinct subgroups, enhancing the understanding of glioma heterogeneity. Integrating newer datasets with multi-omics data, such as copy number variation, could reveal more clusters beyond the current six, leading to more precise molecular stratification.**

