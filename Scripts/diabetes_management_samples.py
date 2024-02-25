# diabetes_samples.py

# Define your samples list
# There are some good samples related to diabetes management guidelines
samples = [
    {
        "inputs": "Question: What are the dietary goals for people with type 2 diabetes?\n\nAnswer: Encourage adherence to the Australian dietary guidelines, emphasizing food quantity and type."
    },
    {
        "inputs": "Question: What's the advised weight loss goal for overweight or obese individuals with type 2 diabetes?\n\nAnswer: Aim for 5-10% weight loss, with greater weight loss measures for those with higher BMI or comorbidities."
    },
    {
        "inputs": "Question: What's the recommended physical activity for children, adolescents, and adults with diabetes?\n\nAnswer: Children and adolescents should aim for at least 60 minutes of moderate-to-vigorous physical activity daily, while adults should strive for 150 minutes of aerobic activity per week."
    },
    {
        "inputs": "Question: What is the advised daily limit for cigarette consumption for individuals with type 2 diabetes?\n\nAnswer: Zero cigarettes per day."
    },
    {
        "inputs": "Question: What is the recommended daily alcohol consumption limit for both men and women with diabetes?\n\nAnswer: Limit alcohol intake to ≤2 standard drinks (20 g of alcohol) per day."
    },
    {
        "inputs": "Statement: What are the target blood glucose levels for fasting and postprandial measurements?\n\nAnswer: Aim for 4-7 mmol/L fasting and 5-10 mmol/L postprandial. Self-monitoring is advised for insulin users."
    },
    {
        "inputs": "Statement: How should self-monitoring of blood glucose (SMBG) frequency be determined for people not on insulin?\n\nAnswer: SMBG frequency should be individualized based on medication type, glycaemic control, and hypoglycaemia risk."
    },
    {
        "inputs": "Statement: When is SMBG recommended during pregnancy for individuals with diabetes or gestational diabetes?\n\nAnswer: SMBG is recommended during pregnancy complicated by diabetes or gestational diabetes."
    },
    {
        "inputs": "Statement: In which medical conditions is SMBG recommended, where HbA1c measurements may be unreliable?\n\nAnswer: SMBG may be helpful in conditions like haemoglobinopathies or other cases with unreliable HbA1c measurements."
    },
    {
        "inputs": "Statement: What is the general target for HbA1c in diabetes management?\n\nAnswer: The target HbA1c level should be individualized, but generally, it's ≤7% (53 mmol/mol)."
    },
    {
        "inputs": "Statement: How is the initiation of lipid-lowering pharmacotherapy determined?\n\nAnswer: Initiation depends on the assessment of absolute cardiovascular disease (CVD) risk, using a risk calculator that considers multiple factors."
    },
    {
        "inputs": "Statement: What are the specified targets for cholesterol levels in diabetes management?\n\nAnswer: Targets include total cholesterol <4.0 mmol/L, HDL-C ≥1.0 mmol/L, LDL-C <2.0 mmol/L (or <1.8 mmol/L with established CVD), and non-HDL-C <2.5 mmol/L."
    },
    {
        "inputs": "Statement: What is the recommended blood pressure target for individuals with diabetes?\n\nAnswer: The recommended blood pressure target is ≤140/90 mmHg, but lower targets may be considered for certain individuals."
    },
    {
        "inputs": "Statement: What is the blood pressure target for people with diabetes and albuminuria/proteinuria?\n\nAnswer: The target for this group is <130/80 mmHg, with individualized treatment and monitoring for side effects."
    },
    {
        "inputs": "Statement: What are the recommended vaccination considerations for individuals with type 2 diabetes?\n\nAnswer: Recommended immunizations include influenza, pneumococcus, diphtheria-tetanus-acellular pertussis (dTpa). Consider hepatitis B if traveling and herpes zoster."
    },
    {
        "inputs": "Statement: Preventing Progression to Type 2 Diabetes:\n\nAnswer: 1. People with impaired glucose tolerance (IGT) or impaired fasting glucose (IFG) should be referred to lifestyle intervention programs to achieve and maintain a 7% reduction in weight and increase moderate-intensity physical activity to at least 150 minutes per week.\n\n2. People with glycated hemoglobin (HbA1c) between 6.0–6.4% may benefit from a structured weight loss and exercise program to reduce their risk of developing type 2 diabetes."
    },
    {
        "inputs": "Statement: Early-Onset Type 2 Diabetes:\n\nAnswer: 1. Children, adolescents, and young adults (aged <25 years) with type 2 diabetes should be referred to an endocrinologist or a specialist physician with an interest in diabetes.\n\n2. For people aged ≥25 years with early-onset type 2 diabetes, consider timely referral to an endocrinologist and/or management through a shared care arrangement."
    },
    {
        "inputs": "Statement: Lifestyle Interventions for Type 2 Diabetes:\n\nAnswer: 1. Encourage physical activity, including aerobic activity for children, adolescents, and adults with type 2 diabetes, and resistance exercise for adults.\n\n2. Promote reduced sedentary behavior.\n\n3. Emphasize the consumption of whole grains and dairy foods for diabetes risk reduction.\n\n4. In overweight or obese individuals with diabetes, recommend a calorie-reduced diet to achieve and maintain a healthier body weight.\n\n5. Weight management medication and metabolic surgery can be considered in certain cases."
    },
    {
        "inputs": "Statement: Smoking Cessation and Alcohol Consumption:\n\nAnswer: 1. Offer smoking cessation advice to all people who smoke.\n\n2. People with diabetes can consume alcohol in moderation but should aim to stay within recommended limits for those without diabetes."
    },
    {
        "inputs": "Statement: Glucose Monitoring:\n\nAnswer: 1. Glycated hemoglobin (HbA1c) measurement should be used to assess long-term blood glucose control.\n\n2. Self-monitoring of blood glucose (SMBG) is recommended for patients with type 2 diabetes using insulin and educated in appropriate alterations in insulin dose.\n\n3. SMBG frequency should be individualized based on glucose-lowering medications, glycaemic control, and risk of hypoglycaemia."
    },
    {
        "inputs": "Statement: Medical Management of Glycaemia:\n\nAnswer: 1. Glucose-lowering medication choice should consider individual factors like comorbidities, hypoglycaemia risk, impact on weight, cost, side effects, and patient preferences.\n\n2. Metformin is preferred over other agents due to its low risk of hypoglycaemia and weight gain.\n\n3. Dose adjustments and/or addition of glucose-lowering medications should be made to achieve target HbA1c within 3–6 months if targets are not met.\n\n4. Less stringent HbA1c goals may be appropriate for certain patients."
    },
    {
        "inputs": "Statement: Type 2 Diabetes and Cardiovascular Risk:\n\nAnswer: 1. Calculate cardiovascular disease (CVD) risk level using evidence-based tools.\n\n2. Adults with specific risk factors may not require absolute CVD risk assessment.\n\n3. High-risk individuals should receive lipid and blood pressure-lowering pharmacotherapy in addition to lifestyle advice.\n\n4. Sodium glucose co-transporter 2 (SGLT2) inhibitors and antihypertensive therapy are recommended in certain cases.\n\n5. Use statins as first-line lipid-lowering therapy."
    },
    {
        "inputs": "Statement: Microvascular Complications:\n\nAnswer: 1. Regularly screen and evaluate for retinopathy, peripheral neuropathy, and foot complications.\n\n2. Implement interventions based on the severity of complications.\n\n3. Provide eye care, neuropathy management, and foot care education.\n\n4. Pharmacological interventions, wound care, and multidisciplinary care are recommended for specific cases.\n\n5. Monitor kidney function with urine ACR and eGFR and optimize blood glucose and blood pressure control to prevent and delay chronic kidney disease (CKD) progression."
    },
    {
        "inputs": "Statement: Mental Health and Type 2 Diabetes:\n\nAnswer: 1. Routinely monitor individuals with diabetes for diabetes distress and consider assessment for other mental health conditions.\n\n2. Collaborative care by inter-professional teams should be provided for people with diabetes and depression.\n\n3. Psychosocial interventions should be integrated into diabetes care plans.\n\n4. Antidepressant medication may be used for acute depression in people with diabetes."
    },

    {
        "inputs": "Statement: Type 2 Diabetes, Reproductive Health, and Pregnancy:\n\nAnswer: 1. Women with pre-pregnancy diabetes should receive pre-conception counseling, aim for optimal glycemic control, discontinue potentially embryopathic medications, and take folate supplements. 2. Pre-pregnancy glycated hemoglobin should be as close to normal as safely possible.3. Monitor and manage diabetes during pregnancy with a multidisciplinary pregnancy team."
    }
]

def get_samples():
    return samples
