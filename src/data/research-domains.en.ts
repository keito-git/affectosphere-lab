// The eight core research domains that frame the lab's affective-AI work.
// AI for Science lives in its own tab.

export type NarrativeBlock = {
  /** Plain English paragraph (no markdown). */
  text: string;
  /** Optional figure paired with this paragraph. */
  figure?: {
    src: string;
    caption: string;
    alt: string;
  };
};

export type ResearchDomain = {
  slug: string;
  title: string;
  image: string;
  summary: string;
  /** Bird's-eye view of the open problems and the breadth of research in this domain. */
  longDescription?: string;
  /** Bird's-eye view of what is gradually being understood across this domain. */
  findings?: string;
  /** Narrative body: alternating text + figure blocks (reads as a story). */
  narrative?: NarrativeBlock[];
};

const fieldImage = (filename: string): string =>
  `/field-images/${encodeURIComponent(filename)}`;

export const researchDomains: ResearchDomain[] = [
  // ===================================================================
  {
    slug: "ethics-philosophy",
    title: "Ethics and Philosophy of Affective AI",
    image: fieldImage("感情AIの倫理と哲学.png"),
    summary:
      "We keep asking who emotion-measuring technologies are for, and how they should be used. We reexamine, in the language of philosophy, the norms that lie between technology and the human.",
    longDescription:
      "Affective AI is a socio-technical system layered out of psychological theory, annotation, modeling, dialogue design, social application, and ethics. Yet existing research tends to advance within each layer in isolation, and structural arguments that cut across layers — or critique that bridges the technical and the humanistic — remain limited. This domain calls for rethinking affective AI not as a single technology but as a layered structure, and for philosophically revisiting the guiding principles of responsible design and social deployment.",
    findings:
      "Stacking layer-by-layer optimizations is not enough: upstream assumptions structurally induce downstream failures. Recurrent patterns of disconnection appear in specific combinations — mismatch between theory and data, cognitive mismatch between models and dialogue interfaces, the splintering of responsibility between technology and ethics — and these are not isolated bugs but cascades that chain across layers. Addressing them requires cross-cutting design principles: longitudinal evaluation, deployment-specific accountability, and preservation of users' interpretive authority.",
    narrative: [
      {
        text:
          "AI that handles emotion is no longer a mere classifier; it is a socio-technical system in which heterogeneous layers — psychological theory, emotion-labeled data, machine learning models, dialogue interfaces, social applications, and ethical responsibility — are stacked on top of each other. To let a computer handle inner experiences such as joy and sadness, one must first choose a psychological theory of what emotion is, then choose a labeling scheme grounded in that theory, then design a model that learns those labels, then design an interface that presents results to the user, and finally articulate the ethical norms required for real-world deployment. These choices form a connected chain. Research in this domain consciously surfaces this layered structure and addresses the normative problems lurking at its seams.",
      },
      {
        text:
          "Within the affective-AI research community, each layer has developed its own methodology and evaluation criteria in relative isolation. Psychologists refine emotion models, data scientists refine annotation schemes, machine learning researchers compete on benchmark accuracy, HCI researchers refine dialogue design, applied researchers push industrial deployment, and ethicists discuss norms. As each specialty deepens, a 'vacuum of responsibility' opens up between layers: problems that should be examined as connected get sliced apart at layer boundaries. This domain treats that pattern of disconnection itself as an object of study.",
      },
      {
        text:
          "Bridging the Silos in Affective AI (2026) is a position paper that organizes affective-AI research as a six-layer pipeline (theory, data, model, dialogue, social application, ethics/evaluation) and diagnoses four recurring patterns of disconnection — 'silo bridges' — between layers. Specifically, it identifies (i) operationalization drift between theory and data (the emotion that theory speaks of and the label that ends up on data diverge), (ii) cognitive mismatch between model and dialogue (model outputs and the user's interpretive frame fail to mesh), (iii) the dissipation of responsibility between technology and ethics (it becomes unclear who is ultimately accountable), and (iv) implicit representativeness assumptions between data and social application (data from specific populations is treated as universal truth).",
        figure: {
          src: "/research-figures/ethics-philosophy/silos.png",
          caption:
            "The six-layer pipeline that constitutes affective AI and the four recurring patterns of disconnection between layers (Bridging the Silos in Affective AI, 2026).",
          alt: "Conceptual diagram of the six-layer affective-AI pipeline and the four silo bridges",
        },
      },
      {
        text:
          "Why does this require a position paper? Because these disconnections are not isolated technical bugs but problems rooted in the very structure of the research community. A model that achieves state-of-the-art accuracy on a particular benchmark may still mislead users at deployment time, and improving the model alone will not fix that. The evaluation axes of the field themselves must be questioned, and a common language that crosses layers must be proposed. This paper aims to put such a cross-cutting perspective before the academic community.",
      },
      {
        text:
          "As a response, the paper proposes five interlocking Design Criteria (DC). DC1, 'theory disclosure,' requires that the adopted emotion theory be explicitly stated in both papers and implementations. DC2, 'intervention boundaries,' requires that the scope of legitimate intervention by affective AI be defined in advance and that the design prevent overreach. DC3, 'longitudinal evaluation,' makes it essential to track effects over time rather than measure accuracy at a single moment. DC4, 'deployment-specific accountability,' requires that — across research prototypes, field trials, and commercial deployment — it be made explicit who bears responsibility for what. DC5, 'preservation of users' interpretive authority,' bakes into the design the principle that the final right to interpret an AI output belongs to the user. These five are not independent rules but a mutually reinforcing normative system.",
      },
      {
        text:
          "DC5 — preservation of users' interpretive authority — sits at the core of the 'emotional sovereignty' concept that this domain puts forward. Emotional sovereignty is the normative position that the final right to interpret, record, and disclose one's own emotions belongs to the person experiencing them. It demands that the asymmetric power relation between an AI saying 'you are angry' and a person replying 'I do not feel that way' be consciously dissolved at the design stage. The concept is positioned as an extension of the right to self-determination in medicine and the right to informational self-control in data protection, and is proposed as a new human-rights notion for the age of affective AI.",
      },
      {
        text:
          "The social and academic reasons that philosophical and normative work on affective AI is needed right now are clear. First, the rapid spread of generative AI is pouring systems that read and respond to emotion into everyday life, and treating their behavior as a problem only after the fact is no longer fast enough. Second, even though emotional data is sensitive personal information, large areas of it are not adequately covered by current law. Third, a shared language among engineers, users, and regulators has yet to mature, and discussion tends to split between technical and ethical registers. Research in this domain aims to present a framework that fills these three gaps.",
      },
      {
        text:
          "This position paper is not a technical paper but a map for re-situating affective AI as a socio-technical system, and it functions as a reference frame for subsequent implementation research and ethical debate. The other domains of our lab — augmenting emotional data, understanding the inside of affective AI, human–AI interaction, business application, and psychological-support development — can each be understood as concrete research carrying one of the layers in this map. Ethics and philosophy serve as the warp thread that runs through all the other research.",
      },
    ],
  },
  // ===================================================================
  {
    slug: "human-emotion-understanding",
    title: "Understanding Human Emotion",
    image: fieldImage("人間の感情理解.png"),
    summary:
      "How do humans actually experience and express emotion in the first place? We re-read the accumulated insights of psychology, cognitive science, and neuroscience as the foundation for AI research.",
    longDescription:
      "Emotion is not a static attribute but a dynamic phenomenon that wavers within context, relationship, and time. Human judgments diverge on the same utterance, and in conversational data more than 70% of annotators assign emotion labels that differ from those of others. Yet machine learning frameworks have averaged out or majority-voted away this disagreement as 'noise.' This domain treats disagreement not as noise but as a signal that reflects the very subjectivity of emotion, and re-reads accumulated psychological theory as the foundation for AI research.",
    findings:
      "Frameworks that retain annotator disagreement and treat it statistically can extract from data structures that are consistent with psychological theory. For instance, transitions between adjacent emotions on Plutchik's wheel are observed in excess, while transitions that flip valence are suppressed — a pattern that aligns with theoretical predictions of emotion dynamics and reproduces across multiple conversational corpora. This suggests that statistical designs respecting the distribution of human judgments offer a new route to psychologically valid emotion understanding.",
    narrative: [
      {
        text:
          "Before we build affective AI, we must understand 'how humans actually experience and express emotion in the first place.' Psychology, cognitive science, and neuroscience have long histories of addressing this question and have proposed numerous theories for classifying, describing, and predicting emotion. This domain aims to re-read those theoretical traditions as the foundation for AI research and to embed them in machine-learning design. For affective AI to escape mere surface-pattern learning and to produce predictions that reflect the structure of human emotional experience, dialogue with psychology is indispensable.",
      },
      {
        text:
          "Several major frameworks dominate psychological theories of emotion. Plutchik's (1980) wheel of emotions arranges eight basic emotions — joy, sadness, anger, fear, disgust, surprise, anticipation, and trust — in a circle and explains complex emotions as mixtures of adjacent ones. Gottman's (1994) interaction analysis coded marital communication in fine detail and showed that specific emotional patterns predict relational collapse. Hatfield and colleagues' (1994) emotional-contagion theory formalized the phenomenon that people automatically mimic others' emotions through facial expression, posture, and voice, and that their own emotions are influenced as a result. These theories all describe how dynamic, relational, and context-dependent emotion is.",
      },
      {
        text:
          "The mainstream of affective-AI research — supervised learning with labels — has nonetheless simplified this dynamic, relational experience into 'discrete-label classification.' Judgments from multiple annotators on the same utterance are aggregated and the majority label is treated as the 'correct answer.' But when one examines the data carefully, in conversational corpora roughly 70% of annotators choose an emotion label that differs from others'. This divergence is not annotator carelessness or incompetence; it is a direct reflection of the inherent subjectivity and polysemy of emotion itself.",
      },
      {
        text:
          "A growing view, in recent years, refuses to erase this disagreement as noise and instead preserves it as a 'signal of emotional subjectivity,' treating it as a probability distribution. By representing training-data ground truth as a distribution rather than a single label, the model can learn the very wavering of human judgment — 'this utterance was judged 60% joy, 30% excitement, 10% surprise.' This lets machine learning aim at 'how faithfully it can reproduce the distribution of human judgments' rather than the binary of right or wrong.",
      },
      {
        text:
          "Bayesian Spectral Emotion Transition Discovery from Multi-Annotator Disagreement (BiSEDD, 2026) extends this direction to the analysis of emotion transitions in conversation. BiSEDD has three stages. The first preserves the distribution of judgments from multiple annotators with a hierarchical Dirichlet–Multinomial model and estimates a posterior distribution over the emotion-transition probability matrix. This lets us treat 'how easily one emotion shifts into another' as a probability distribution rather than a point estimate.",
        figure: {
          src: "/research-figures/human-emotion-understanding/bayes-spectral.png",
          caption:
            "Overview of BiSEDD. Annotator disagreement is preserved as a Bayesian posterior, and emotion transitions are analyzed in terms of 'persistence' and 'contagion' (Bayesian Spectral Emotion Transition Discovery, 2026).",
          alt: "Three-stage pipeline for emotion-transition discovery via Bayesian posteriors and spectral decomposition",
        },
      },
      {
        text:
          "In the second stage, the estimated transition matrix is treated as a graph Laplacian (a mathematical operator that analyzes structure on a graph), and a spectral decomposition (eigenvalue/eigenvector decomposition) is performed. This makes it possible to separate the dynamics of emotion transition, mathematically, into two psychologically meaningful components: 'persistence' (how much one's own emotion continues by inertia) and 'contagion' (how much one is influenced by others' emotions). Spectral decomposition is widely used in signal processing and physics, and this work applies it to the temporal dynamics of emotion.",
      },
      {
        text:
          "In the third stage, the resulting components are compared with psychological theory. Across five conversational corpora including EmotionLines, transitions between emotions adjacent on Plutchik's wheel — for example disgust to anger — are observed in excess, while transitions that flip valence — for example joy to anger — are clearly suppressed. Patterns of 'relationship-collapse emotion transitions' predicted by Gottman's interaction analysis are also detected. This shows that a design that treats annotator disagreement as information can, for the first time, statistically extract from data structures consistent with predictions from Plutchik's wheel, Gottman's interaction analysis, and Hatfield's emotional-contagion theory.",
      },
      {
        text:
          "The implication is that 'statistical designs that respect the distribution of human judgments' can serve as a new route to psychologically valid emotion understanding. Variability in annotator judgment is not measurement error but the very diversity of emotional interpretation across human populations. Preserving it through statistical processing lets AI learn 'the distribution of interpretations that a population produces' rather than 'the judgment that the average human would make.' This domain is positioned as foundational research for a next-generation affective AI that respects the subjectivity of emotion.",
      },
    ],
  },
  // ===================================================================
  {
    slug: "data-augmentation",
    title: "Augmenting Emotional Data",
    image: fieldImage("感情データの拡張.png"),
    summary:
      "We explore methods that augment and complete ambiguous, polysemous emotion labels while preserving their uncertainty — enabling faithful learning even from sparse annotation.",
    longDescription:
      "Affective-AI training requires emotion-labeled data produced by humans, yet collection is constrained both structurally and ethically: psychological burden on annotators, privacy, annotator idiosyncrasy (individual bias), and difficulty of collecting data from particular populations such as children or older adults. This domain studies non-individual data generation that does not rely on personalized collection, together with methods that augment existing data semantically and distributionally. Approaches include LLM-based synthesis, knowledge-driven conditional generation, persona conditioning, and developmental-stage adaptation, all running in parallel.",
    findings:
      "LLM-based emotion-data generation can — beyond mere paraphrasing — reach distributional alignment and diversity comparable to real data when geometric, knowledge-based, persona-based, and developmental controls are combined. 'Directional control' that targets underpopulated emotional regions, 'knowledge-driven' designs that embed human knowledge as statistical features, and multi-stage 'persona conditioning' have emerged as keys to achieving distributional alignment and diversity simultaneously. These open paths to deploying affective AI even in areas where collection is ethically difficult.",
    narrative: [
      {
        text:
          "Affective-AI training requires emotion-labeled data produced by humans, but collection is not merely a matter of workflow efficiency — it runs into structural and ethical constraints. First, emotion annotation can impose a psychological burden on annotators: repeatedly reading and judging text or video laced with pain, sadness, and fear can produce secondary mental harm. Second, since emotional data describes a person's interior directly, demands for privacy protection are extreme. Third, there are populations — children, older adults, specific cultural groups — from which direct collection is ethically difficult. This domain centers on the question of how to secure the data that affective AI needs while honoring these constraints.",
      },
      {
        text:
          "It is useful to organize three concepts: 'personality-dependent' versus 'personality-independent' collection, and 'semantic augmentation.' Personality-dependent collection is the traditional approach of obtaining emotion labels directly from specific people; their subjectivity and individual bias enter the result directly. Personality-independent generation synthesizes data without depending on specific individuals — LLM-based generation and knowledge-driven conditional generation are representative. Semantic augmentation supplements and extends distributions while preserving the semantic and statistical structure of existing data, and is used for imbalance correction and domain adaptation. This domain combines these three concepts to seek designs that satisfy both ethics and accuracy.",
      },
      {
        text:
          "Emotional datasets always carry imbalance: dense around some classes and full of holes around others. Frequent emotions such as 'joy' and 'sadness' attract large numbers of samples, while rare emotions such as 'contempt' and 'awe' yield only a few. This imbalance causes machine-learning models to misclassify minority classes. CIEGAD (Cluster-conditioned Interpolation/Extrapolation Geometric Augmentation for Data, 2025) addresses this by geometrically controlling the direction of 'interpolation (filling holes)' and 'extrapolation (extending peripheries)' within each cluster and asking an LLM to perform conditional generation. Concretely, interpolating between existing samples in the embedding space fills holes, and extrapolating outside the cluster widens the periphery. The approach stably improves F1 and recall on minority classes.",
        figure: {
          src: "/research-figures/data-augmentation/ciegad.png",
          caption:
            "Concept diagram of CIEGAD. Cluster-conditioned interpolation and extrapolation are geometrically controlled to supplement imbalanced emotion data (Geometric Control-Based Data Augmentation, 2025).",
          alt: "Concept diagram of geometric-control data augmentation by cluster-conditioned interpolation and extrapolation",
        },
      },
      {
        text:
          "KDDA (Knowledge-Driven Data Augmentation, 2025) is a framework that, instead of collecting emotion data directly from individuals, converts human knowledge about a target domain into statistical features and uses them to condition LLM generation. For a domain such as 'workplace stress,' it builds a 'domain profile' from features specific to that domain — vocabulary frequencies, typical situations, characteristic emotion patterns — and uses it to condition the LLM. Generated data is doubly filtered by lexical-level overlap suppression and statistical consistency evaluation based on Negative Log-Likelihood (NLL), removing low-quality samples. As a result, an emotion classifier trained solely on synthetic data achieved the closest distribution to real data on 9 of 12 metrics — an example of a personality-independent generation pipeline that avoids personality-dependent collection.",
        figure: {
          src: "/research-figures/data-augmentation/kdda.png",
          caption:
            "Data-generation pipeline of KDDA. Using a domain profile built from domain knowledge as the criterion, generated data is double-filtered statistically and lexically (KDDA, 2025).",
          alt: "Overall diagram of the knowledge-driven emotion-data generation framework",
        },
      },
      {
        text:
          "PersonaGen (2025) is a method that progressively conditions an LLM on multi-layer personas — age, occupation, personality, cultural background — to generate emotion expressions that are socio-culturally consistent. Even 'sadness' is articulated differently by a teenage student and a sixty-year-old physician. PersonaGen stacks conditioning in three stages — attributes, socio-cultural background, situational context — and reproduces stylistic differences consistent with the persona. As a result, the same emotion label yields diverse expressions appropriate to the character speaking, and downstream tasks achieve performance approaching real data. Multi-stage persona conditioning is effective for jointly securing expressive diversity and emotion-label consistency.",
        figure: {
          src: "/research-figures/data-augmentation/personagen.png",
          caption:
            "Multi-stage persona conditioning of PersonaGen. Conditions are stacked on the LLM in the order attribute → socio-cultural background → situational context, producing emotion expressions consistent with the persona (PersonaGen, 2025).",
          alt: "Multi-stage persona-conditioned emotion-generation framework of PersonaGen",
        },
      },
      {
        text:
          "Reproducing Developmental Features and Preserving Semantics in Child-Style Text Generation Using LLM (2025) responds to the ethical difficulty of collecting data directly from children. Adult-oriented Japanese sentences are rewritten across sixteen developmental stages from first grade through fourth-year university, and the work examines semantic preservation and the reproducibility of developmental features. With few-shot prompting, semantic similarity is maintained at 0.82–0.99 while kanji-to-kana ratios and readability indices change in step with grade level. Without accessing children directly, the approach shows the feasibility of synthesizing the 'child-like' style needed for educational affective AI and children's content design.",
      },
      {
        text:
          "Beyond these technical maneuvers, emotional data collection carries ethical problems that they alone cannot resolve. First, asymmetric power between collector and provider: the relation in which researchers or companies elicit emotion from a data provider inherently weakens informed consent. Second, secondary-use problems: emotional data collected for one study is often reused in another context where the provider could not have anticipated that use. Third, difficulty of collection from specific populations can result in excluding those populations from the benefits of AI (lack of representativeness). Research in this domain runs in parallel with these ethical issues and seeks balance points through personality-independent generation.",
      },
      {
        text:
          "The implication is that LLM-based emotion-data generation, when combined with geometric, knowledge-based, persona-based, and developmental controls, can — beyond mere paraphrasing — reach distributional alignment and diversity comparable to real data. In particular, 'directional control' that targets underpopulated emotional regions (CIEGAD), 'knowledge-driven' designs that embed human knowledge as statistical features (KDDA), 'persona conditioning' that builds personas in multiple stages (PersonaGen), and 'age adaptation' that controls developmental stage (child-style) each complement data limitations along different axes. These techniques are opening paths to deploying affective AI even in domains where collection is ethically difficult.",
      },
    ],
  },
  // ===================================================================
  {
    slug: "interpretability",
    title: "Understanding the Inside of Affective AI",
    image: fieldImage("感情AIの内部理解.png"),
    summary:
      "We unravel what models actually base their emotion judgments on and make the underlying behavior visible.",
    longDescription:
      "Affective AI, and Large Language Models (LLMs) in particular, may look as if they are assigning labels correctly on the surface, yet the basis for their judgments is opaque. For emotion tasks, where subjectivity is essential, we must quantify — from distributional and Bayesian perspectives — whether models reproduce the 'hesitation' and 'wavering' of humans, whether confidence aligns with correctness, and how internal knowledge is elicited and used. This domain advances research that clarifies not just output-label accuracy but the shape of the output distribution, the structure of uncertainty, and how internal knowledge is brought to bear.",
    findings:
      "Large-scale distributional analyses show that LLMs capture the dominant emotion label (the majority answer) but cannot structurally reproduce the 'shape of wavering' among human annotators. The quality of the gap differs between lexically explicit emotions and emotions that require contextual inference, and post-hoc calibration has limits. Meanwhile, combining Bayesian sampling (cSG-MCMC) with soft-label learning provides a framework that separates data-borne from knowledge-borne uncertainty, enabling more honest uncertainty expression for subjective tasks.",
    narrative: [
      {
        text:
          "Affective AI, and Large Language Models (LLMs) in particular, may appear to assign labels correctly on the surface, yet the basis for their judgments is opaque. This is the classical 'black-box problem' of deep learning: what happens inside the model, and on which input features the output depends, cannot be directly observed by humans. In affective AI, black-boxness is not merely a technical inconvenience but harbors a serious ethical concern. If the AI cannot explain why it ruled 'you are sad,' the user has no basis for accepting or rejecting that ruling. This domain aims to unravel the inside of affective AI and make the underlying behavior visible.",
      },
      {
        text:
          "Another distinctive feature of emotion tasks is that there is no objectively fixed 'correct answer' — they are subjective problems. The question 'is this text anger or disgust?' divides human annotators. Therefore, evaluation of affective AI should be measured not by agreement with a single ground-truth label but by how faithfully the model reproduces the distribution of human judgments. Concretely, internal understanding must be advanced from three perspectives: (i) whether the model reproduces human 'hesitation' and 'wavering,' (ii) whether confidence aligns with correctness (calibration), and (iii) what knowledge is elicited and how it is used to judge.",
      },
      {
        text:
          "An important concept to organize here is 'calibration.' Calibration measures the degree to which a model's stated confidence (probability) matches its actual accuracy. For example, if a model predicts many cases as 'emotion A with 80% confidence' and 80% of those turn out correct, the model is calibrated. Many deep-learning models fall into overconfidence: they assert 90% confidence while being correct only 70% of the time. For subjective tasks such as emotion, whether the model can correctly express a 'hesitant' state — that is, whether it can output appropriately low confidence — is the key to reliability.",
      },
      {
        text:
          "LLMs Capture Emotion Labels, Not Emotion Uncertainty (2026) examined, in a large-scale experiment spanning four models and 640,000 responses, the extent to which LLMs as emotion annotators can reproduce human judgment distributions. The design had LLMs annotate items in multiple emotion datasets including GoEmotions many times and compared the output distributions with the judgment distributions of human annotator populations using distributional metrics (KL divergence, Earth Mover Distance, etc.). The result: representative labels broadly agree, but the 'shape of wavering' among annotators — the shape of the judgment distribution — is not reproduced.",
        figure: {
          src: "/research-figures/interpretability/llm-gaps.png",
          caption:
            "Framework for distributional analysis of the human–LLM emotion-judgment gap (LLMs Capture Emotion Labels, Not Emotion Uncertainty, 2026).",
          alt: "Overall framework for analyzing human–LLM emotion-judgment distributional gaps",
        },
      },
      {
        text:
          "A particularly interesting finding is that the quality of the gap differs by emotion category. For emotions that are lexically explicit (where a keyword appears in the text), such as 'gratitude' and 'love,' LLM judgments broadly agree with humans'. For emotions that require contextual inference (where one must read between the lines), such as 'approval' and 'realization,' the LLM and human judgment distributions diverge widely. Furthermore, post-hoc calibration methods such as temperature scaling and Platt scaling reduce the gap by at most 14%. This means there is a structural limit to LLMs' understanding of emotion that cannot be captured by surface label-prediction accuracy.",
      },
      {
        text:
          "Uncertainty Decomposition via Cyclical SG-MCMC and Soft-label Learning for Subjective NLP (2026) proposes a Bayesian approach to this problem. The key concepts are the decomposition into 'epistemic uncertainty' and 'aleatoric uncertainty.' Epistemic uncertainty is the kind that arises from the model's lack of knowledge and can in principle be reduced by adding data. Aleatoric uncertainty is intrinsic to the data and is not reduced by adding more data. In subjective tasks such as emotion, the two are mixed, and separating them is key to 'honest uncertainty expression.'",
      },
      {
        text:
          "The proposed method combines cSG-MCMC (cyclical Stochastic Gradient Markov Chain Monte Carlo) — a Bayesian sampling technique that varies the learning rate cyclically while drawing from the posterior over model parameters — with soft-label learning that learns the human annotator distribution as a probability distribution. cSG-MCMC efficiently captures epistemic uncertainty, while soft-label learning expresses aleatoric uncertainty on the data side. Combining the two yields a structural decomposition of the two components of uncertainty. On 28-emotion GoEmotions, the approach surpasses existing Bayesian methods such as MC Dropout and Deep Ensemble on annotator-distribution agreement, selective prediction performance, and per-category uncertainty correlations.",
      },
      {
        text:
          "The implication is that the internal understanding of affective AI requires evaluation axes distinct from 'improving accuracy.' Concretely, three perspectives are being established as reliability indicators when deploying affective AI in society: (i) distributional alignment (how well the model output distribution matches the human judgment distribution), (ii) calibration quality (how well confidence matches accuracy), and (iii) structural decomposition of uncertainty (the separation of epistemic and aleatoric components). These perspectives connect tightly to other domains in our lab, especially to safety design in applied development and accountability discussions in ethics.",
      },
    ],
  },
  // ===================================================================
  {
    slug: "emotion-recognition",
    title: "Emotion Recognition by AI",
    image: fieldImage("AIによる感情の認識.png"),
    summary:
      "Foundational recognition research that estimates emotion distributions from text, speech, and physiological signals — aiming for designs that handle uncertainty rather than point estimates.",
    longDescription:
      "Emotion recognition covers many modalities — text, speech, physiological signals, video — and many targets, from binary positive/negative judgment to two-faced expressions such as sarcasm, drivers' psychological states, and context-dependent emotion interpretation. Because single-model point estimates wash out cultural polysemy, annotator disagreement, and minority opinion, recent work studies designs that combine multiple perspectives, multiple experts, and multi-stage reasoning, embeds causal structure grounded in cognitive science, and produces predictions with uncertainty.",
    findings:
      "The key to improving emotion recognition appears to lie not in single-model one-shot prediction but in decomposing inference across perspectives, experts, and stages. For sarcasm understanding, the 'gap between literal and intended meaning' and the cognitive chain of 'observation → norm → intent' are explicitly built into the model structure. For driving support, the causal chain 'perception → judgment → emotion → action' is incorporated. LLMs deliberating among themselves — like a circulating notice or a casual chat — keep runaway confidence in check. These designs improve not just accuracy but also explainability and the quality of uncertainty expression.",
    narrative: [
      {
        text:
          "Emotion recognition is a central task in affective AI and covers many modalities including text, speech, physiological signals, and video. Text-based emotion recognition is widely used in social-media analysis and customer support; speech-based recognition appears in call centers and voice assistants; physiological-signal recognition (heart rate, electrodermal activity, EEG) is deployed in medical and wellbeing applications; and video-based recognition has spread to driver support and educational assessment. Each modality has distinct strengths: text excels in semantic richness, speech offers prosody, physiological signals reach subconscious affective states, and video provides dynamic information from facial expression and posture.",
      },
      {
        text:
          "Targets range from simple binary positive/negative judgment to two-faced expressions such as sarcasm, drivers' psychological states, and context-dependent emotion interpretation. Particularly difficult are cases in which expression and intent diverge. Sarcasm is the prototypical example — positive on the surface, negative in intent. Cultural polysemy also matters: whether the Japanese 'kekkō desu' is acceptance or refusal depends on context. Further complications include annotator disagreement and the neglect of minority opinion. Single-model point estimates wash out all of this complexity.",
      },
      {
        text:
          "Recent work has succeeded with designs that decompose inference across multiple perspectives, multiple experts, and multiple stages rather than producing one-shot predictions from a single model. Research in this domain proceeds in four directions: (i) approaches that embed cognitive-scientific accounts of human reasoning into the model structure, (ii) designs in which multiple LLM agents deliberate, (iii) the incorporation of uncertainty expression via methods such as Evidential Deep Learning, and (iv) lightweighting and robustness tailored to modality characteristics. Below we introduce representative studies in turn.",
      },
      {
        text:
          "World Model Inspired Sarcasm Reasoning with LLM Agents (WM-SAR, 2026) decomposes sarcasm understanding into the human cognitive process of 'observation → norm prediction → gap detection → intent inference,' and assigns each stage to a separate LLM agent. The notion of a 'world model' here refers to the internal representation of reality that humans maintain in order to predict the outcomes of actions; sarcasm is recognized through the gap between a 'norm-based prediction grounded in the world model' and the actual utterance. The observation agent describes the situation, the norm-prediction agent predicts 'what one would normally say,' the gap-detection agent extracts the difference from the actual utterance, and the intent-inference agent estimates the underlying intent. A lightweight regression model makes the final decision. Beyond surpassing existing methods in accuracy, the system can structurally explain 'where the gap arose.'",
        figure: {
          src: "/research-figures/emotion-recognition/wm-sar.png",
          caption:
            "Structure of WM-SAR. Different LLM agents handle observation, norm prediction, gap detection, and intent inference, reasoning about sarcasm in a world-model style (WM-SAR, 2026).",
          alt: "World-model-inspired multi-agent sarcasm-reasoning architecture of WM-SAR",
        },
      },
      {
        text:
          "Cognitive-Causal Multi-Task Learning (CauPsi, 2026) directly structures cognitive-scientific insight into driving-support recognition tasks. The 'cognitive-causal chain' here refers to the ordered psychological process — perception → judgment → emotion → action — that humans go through when acting. CauPsi links four tasks — traffic-situation recognition, vehicle-operation prediction, emotion estimation, and behavior prediction — as multi-task learning that follows this causal chain. Specifically, the intermediate representations of lower tasks propagate as conditions to higher tasks, and in particular the psychological state estimated from the driver's face and posture conditions all tasks. With about 5M parameters, the model achieves 82.7% average accuracy and improves over prior methods especially on emotion (+3.7%) and behavior (+7.5%). It is a fine example of translating cognitive science directly into model structure.",
        figure: {
          src: "/research-figures/emotion-recognition/caupsi.png",
          caption:
            "Structure of CauPsi. The cognitive-causal chain is built in as the structure of four tasks, and psychological-state conditioning is supplied to all tasks (CauPsi, 2026).",
          alt: "Overall architecture of CauPsi cognitive-causal multi-task learning",
        },
      },
      {
        text:
          "A Multi-Agent Probabilistic Inference Framework Inspired by Kairanban-Style CoT (2025) is a distinctive attempt that imports a Japanese cultural deliberation process into machine reasoning. The 'kairanban' is a Japanese tradition in which a document is passed in turn around a neighborhood association so members can add their opinions, and the paper translates this into the Kairanban Chain of Stamps (KCS), a design in which multiple LLMs append opinions in turn. This is followed by 'idobata conversation' (IBC), a stage in which multiple LLMs exchange opinions freely. The two-stage discussion suppresses runaway confidence (overconfidence by a single model) while preserving variance in predictions, achieving more careful emotion estimation. It is an interesting design study showing that a cultural deliberation process can function as a bias-correcting mechanism.",
        figure: {
          src: "/research-figures/emotion-recognition/kairanban.png",
          caption:
            "Multi-agent inference framework that combines kairanban-style CoT with idobata conversation (Kairanban-IBC, 2025).",
          alt: "Multi-agent emotion-inference framework combining kairanban and idobata conversation",
        },
      },
      {
        text:
          "Dual-Branch Feature Extraction via Discrepancy-Aware Fusion with Evidential Deep Learning for Sarcasm Detection (DBDA-EDL, 2025) represents sarcasm in two parallel streams — 'literal' and 'intended' — and explicitly extracts the mismatch between them. The Evidential Deep Learning (EDL) introduced here is a method that directly outputs the parameters of a Dirichlet distribution rather than ordinary class probabilities, simultaneously expressing predictive confidence and uncertainty. DBDA-EDL extracts the discrepancy between literal and intended representations as a fused feature and uses EDL to output predictive confidence at the same time. For ambiguous sarcasm, it realizes an 'honestly hesitant model' that returns a modest confidence.",
        figure: {
          src: "/research-figures/emotion-recognition/dual-branch.png",
          caption:
            "Structure of DBDA-EDL. Sarcasm detection and uncertainty estimation via Dual-Branch / Discrepancy-Aware Fusion / Evidential Deep Learning (DBDA-EDL, 2025).",
          alt: "DBDA-EDL dual-stream feature extraction and discrepancy-fusion sarcasm-detection architecture",
        },
      },
      {
        text:
          "C-DIRA (2025) redesigns driver-behavior recognition for in-vehicle cameras under the industrial requirement of jointly achieving lightweighting and robustness. In-vehicle environments pile up problems that are invisible in the lab: limited compute, diverse lighting, individual driver differences, varying camera positions. C-DIRA addresses these with two ideas. First, 'dynamic ROI routing' first classifies the entire image and only narrows down to important regions (Regions of Interest) for difficult scenes. Second, 'domain-invariant adversarial learning' adversarially trains the model to cancel out differences in driver and lighting environment. With only 2M parameters, the model achieves 99.2% accuracy together with robustness to domain shift.",
        figure: {
          src: "/research-figures/emotion-recognition/cdira.png",
          caption:
            "Structure of C-DIRA. Lightweight driver-behavior recognition combining dynamic ROI routing with domain-invariant adversarial learning (C-DIRA, 2025).",
          alt: "Structural diagram of C-DIRA's dynamic ROI routing and domain-invariant learning",
        },
      },
      {
        text:
          "The implication is that the key to improving emotion recognition lies not in improving single-model one-shot prediction but in decomposing inference across 'perspectives, experts, and stages.' Sarcasm understanding improves via two streams of literal and intended (DBDA-EDL) and via the chain of norm prediction and intent inference (WM-SAR); driving recognition improves via the cognitive-causal chain (CauPsi) and via a cultural deliberation process (Kairanban). Each simultaneously improves accuracy, explainability, and the quality of uncertainty expression. These designs connect directly to the concern raised in our lab's 'Understanding the Inside of Affective AI' domain — that evaluation must be multifaceted, not merely accuracy-based — and dialogue between design and evaluation is advancing across domains.",
      },
    ],
  },
  // ===================================================================
  {
    slug: "human-ai-interaction",
    title: "Affective AI and Human Interaction",
    image: fieldImage("感情AIと人間のインタラクション.png"),
    summary:
      "How should we design the place where people and models face each other? Self-reflection, dialogue, and the problem of co-presence.",
    longDescription:
      "When affective AI enters society, new relations arise between humans and models. Does it support self-reflection? Does it invite people to defer judgment to it? Does it become a partner in co-presence? Designing that interface requires a logic distinct from technical accuracy. This domain is beginning to launch research that rethinks the relationship itself, across dialogue design, self-reflection support, and HCI mediated by emotion.",
    findings:
      "This domain is ongoing. Self-reflection support functions in dialogue AI and design principles for co-presence interfaces are being formulated. In emotion-mediated HCI, a hypothesis is taking shape that designs in which AI functions as a 'mirror' or 'conversational partner' — rather than as a 'judge' — contribute to deepening self-understanding. Details will be released as work progresses.",
    narrative: [
      {
        text:
          "When affective AI enters society, new relations arise between humans and models. Our relations with computers have so far been primarily instrumental — input commands, receive results. But affective AI has the potential to construct deeper relationships as an entity that reads the user's interior, responds to the user, and influences the user's emotion. This domain centers on the question of how to design the 'place' where people and AI face each other through emotion. The object of study is not the improvement of technical accuracy but a logic distinct from it — the design of the relationship itself.",
      },
      {
        text:
          "There are several possible stances for the relationship between people and affective AI. The first is the position of 'supporter of self-reflection,' in which the AI helps the user understand and articulate their own emotion. The second is the position of 'authority to which judgment is deferred,' in which the user acts according to the AI's judgment. The third is the position of 'partner in co-presence,' in which the AI functions not as a judge or a supporter but simply as a presence that is there. Each stance carries different design principles and ethical implications. Our lab emphasizes especially the first and the third — stances that respect the non-intrusiveness of AI.",
      },
      {
        text:
          "Self-reflection support is a design principle in which the AI does not hand the user an 'answer' but supports the process through which the user arrives at insight on their own. In the Rogerian tradition of psychotherapy (client-centered therapy), the therapist refrains from offering answers and, by reflecting, summarizing, and clarifying the client's speech, deepens the client's self-understanding. When affective AI plays a similar role, the AI functions as a 'mirror' rather than as a judge: it reflects the user's emotional expression, offers help in objectifying their own emotion, but leaves the final interpretation and meaning-making to the user. This is also a practical application of the earlier 'emotional sovereignty' concept.",
      },
      {
        text:
          "Co-presence interfaces are a newer design area. The AI is designed as a presence that runs continuously, shares space with the user, and responds quietly only when needed. It sits in the lineage of smart speakers and ambient computing, but for affective AI it is not mere voice response: adjusting the sense of distance according to the user's emotional state is key. The design target is behavior tuned to emotion — drawing close when the user is down, stepping back when they are focused, presenting options when they are conflicted. This is at the frontier of HCI (Human–Computer Interaction) mediated by emotion.",
      },
      {
        text:
          "At present this domain is at a stage of launching projects, and the number of published papers is limited. The problem statement, however, is clear: the more affective AI is deployed in society, the more the relationship itself between humans and AI must be designed. Unlike other domains that chase technical accuracy, this domain develops research at the intersection of design and ethics — 'how to make highly accurate AI coexist with people.' It plays the role of binding together, in implementation, the emotional-sovereignty concept of our ethics-and-philosophy domain and the psychological-support design of our applied-development domain.",
      },
    ],
  },
  // ===================================================================
  {
    slug: "business",
    title: "Affective AI and Business",
    image: fieldImage("感情AIとビジネス.png"),
    summary:
      "We re-frame the meeting point of uncertainty, acceptance, and ethics in industrial deployment as practitioner knowledge.",
    longDescription:
      "When affective AI is built into corporate activity, technical accuracy alone is not enough in scene after scene. User acceptability, operational uncertainty, accountability, and the ethical considerations specific to services that touch emotion — these multiple axes of constraint must be satisfied simultaneously. This domain takes as its object the design of affective AI not for 'selling' but for 'delivering while protecting people,' and explores diverse applications including recommendation, content moderation, and decision support.",
    findings:
      "Studies of multimodal recommendation and consumer protection have made the essentials of implementing affective AI visible: designs that extract latent orientations such as 'lifestyle,' techniques that adjust the affective intensity of stimulating information while preserving meaning, and longitudinal monitoring of use context. These are effective for simultaneously satisfying technical accuracy and social acceptability.",
    narrative: [
      {
        text:
          "When affective AI is built into corporate activity, technical accuracy alone is not enough in scene after scene. A recommender system reads the user's emotion too well and invades privacy; content delivery competes on stimulation and worsens users' mental state; customer-service AI accumulates personal emotional information and leaks it to third parties — all are problems that surface only in deployment. This domain takes as its object the design of affective AI not for 'selling' but for 'delivering while protecting people,' and explores diverse applications including recommendation, content moderation, and decision support.",
      },
      {
        text:
          "Industrial deployment imposes constraints absent in research prototypes, all at once. First, user acceptability: even technically excellent systems will not spread if users find them 'creepy.' Second, operational uncertainty: in real environments, inputs unlike training data flow in daily, and model behavior becomes unpredictable. Third, accountability: when something goes wrong, commercial deployment requires clarity about who is responsible. Fourth, ethical considerations specific to emotion-related services: because they intervene in users' vulnerable moments, they demand a higher ethical bar than ordinary IT services. This domain advances design research that handles these constraints simultaneously.",
      },
      {
        text:
          "Commercial use of emotional data carries distinctive ethical problems. First, although emotional data is sensitive personal information, in many cases it is not explicitly covered by current law. Second, the accuracy of emotion prediction is also the accuracy of manipulating users, and it can distort decision-making through micro-targeted advertising and the like. Third, it is practically difficult for users to refuse the acquisition of emotional data entirely (webcams, microphones, and text are everywhere). This domain explores technical and normative designs that respond to these problems together with concrete applications.",
      },
      {
        text:
          "MALLET (Multi-Agent LLM-based Emotion Tempering, 2026) is a consumer-protection framework that delivers stimulating news and similar expression to users with reduced affective intensity while preserving meaning. The background is the concern that the 'attention economy' of social media and news distribution captures attention by stimulating people's emotion, ultimately worsening users' mental state. MALLET consists of four LLM agents. An emotion-analysis agent measures the affective intensity of the input text, a tempering agent rewrites the text to lower its affective intensity while preserving meaning, a monitoring agent tracks the user's emotion history weekly, and a guide agent produces individualized feedback. On 800 AG News items, MALLET achieves stimulation-score reductions of up to 19.3% while keeping SBERT similarity at 0.83 or above, jointly preserving meaning and tempering emotion.",
        figure: {
          src: "/research-figures/business/mallet.png",
          caption:
            "Structure of MALLET. Four LLM agents share the roles of emotion analysis, tempering, monitoring, and guidance (MALLET, 2026).",
          alt: "Overall diagram of the MALLET multi-agent system for emotion tempering in consumer protection",
        },
      },
      {
        text:
          "GNN-Enhanced Multimodal Fusion (2025) rethinks user personalization through the concrete application of meal recommendation. Conventional meal recommenders are dominated by collaborative filtering that recommends similar recipes from past recipe ratings, but this ignores the user's long-term health goals and lifestyle. This work integrates diverse information — food images, nutritional data, ingredient composition, and cooking methods — using a Graph Neural Network (GNN). A GNN is a deep-learning method that performs representation learning while taking relations between nodes into account, and it can consistently handle diverse relations such as ingredient-to-dish and dish-to-nutrition. Furthermore, contrastive learning extracts the user's 'lifestyle' as a latent representation. As a result, the model surpasses existing methods on AllRecipes data and demonstrates the feasibility of food recommendations consistent with health goals.",
        figure: {
          src: "/research-figures/business/gnn-recipe.png",
          caption:
            "Structure of GNN-Enhanced Multimodal Fusion. Visual, lifestyle, and taste features are fused with HGT to recommend health-oriented recipes (2025).",
          alt: "Concept diagram of GNN-enhanced multimodal fusion for health-recipe recommendation",
        },
      },
      {
        text:
          "Both studies share the orientation of designing AI not for 'selling' but for 'delivering while protecting people.' MALLET deliberately reduces affective intensity to prioritize long-term user wellbeing over short-term attention maximization. GNN-Enhanced Multimodal Fusion prioritizes long-term lifestyle alignment over short-term preference matching. Both are studies that articulate the 'point where accuracy and ethics balance' in industrial deployment as concrete design choices. This domain will concretize, application by application, this 'people-centered way of deploying affective AI.'",
      },
    ],
  },
  // ===================================================================
  {
    slug: "affective-ai-art",
    title: "Affective AI and Art",
    image: fieldImage("感情AIとアート.png"),
    summary:
      "Art as the place where emotion and expression meet — a domain in which AI moves among three positions: 'making,' 'reading,' and 'inspiring.'",
    longDescription:
      "Art is the densest expression of emotion and at the same time the most open site of interpretation. With the rise of generative AI, three positions have come into being at once: AI as a tool that assists human expression, AI that interprets human works, and AI that itself generates works. This domain explores how AI that handles emotion can function in the territory of art, and how it can extend or constrain human creativity and sensibility.",
    findings:
      "The intersection of affective AI and art is ongoing, and themes are emerging: ethics of creation by generative AI, extension of human sensibility, pluralization of work interpretation. The perspective that AI can occupy not only the position of 'making' but also of 'reading' and 'inspiring' is growing in importance for both creative support and the realms of criticism and education. Research content and findings will be released as work progresses.",
    narrative: [
      {
        text:
          "Art is the densest expression of emotion and at the same time the most open site of interpretation. Painting, music, literature, and the performing arts all transmit the creator's emotional experience to the receiver through a medium and evoke emotional experience on the receiver's side. Since antiquity, art has functioned as a cultural device for understanding and sharing human emotion. The intersection of affective AI and art is a domain that adds a new technical layer to this cultural tradition. This domain explores how AI that handles emotion can function in the territory of art and how it can extend or constrain human creativity and sensibility.",
      },
      {
        text:
          "With the rise of generative AI, the positions AI can take with respect to art can be organized into three large categories. The first is 'making,' in which AI directly generates artworks. Generative AI such as Stable Diffusion, DALL-E, Sora, and Suno produces images, video, and music from textual descriptions and has dramatically lowered the threshold of creation. The second is 'reading,' in which AI interprets existing artworks and extracts emotion, meaning, and context. Emotion analysis of paintings, analysis of affective structure in music, and extraction of emotion curves from literary texts fall here. The third is 'inspiring,' in which AI takes on the supportive role of helping and prompting human creation — idea generation, style transfer, critical feedback. Our lab pursues research that moves among these three positions.",
      },
      {
        text:
          "Numerous serious ethical issues surround AI art. First, copyright of training data: generative AI uses large numbers of existing works as training data, yet their creators have typically not consented to such use. Second, ownership of copyright in AI-generated works: which entity owns the copyright in works generated by AI is a question that is still being worked out across jurisdictions. Third, the problem of substituting for or suppressing human creativity: if cheap AI generation becomes commonplace, the economic foundation of human artists can be destroyed. Fourth, cultural diversity: generative AI reflects the bias of its training data and tends to generate output biased toward particular cultural styles, which can reduce cultural diversity as a result. This domain proceeds in parallel with these issues and conducts art research that draws on the distinctive features of affective AI.",
      },
      {
        text:
          "The distinctive contribution affective AI can offer to art is 'fine-grained interpretation of emotion' and 'adjustment of expression according to emotion.' Examples include museum interfaces that change how a work is presented according to the user's current emotional state, tools that visualize the emotion curves of literary works to support criticism, and systems that analyze the affective structure of music to support composition — there are many possible combinations of affective AI and art. The techniques accumulated in our lab's domains of emotion recognition, data augmentation, and interpretability can all serve as foundations for application in art.",
      },
      {
        text:
          "At present this domain is at a stage of launching projects, and the number of published papers is limited. Nonetheless, the intersection of affective AI and art is positioned as an important axis for the lab's future development. In parallel with exploring technical possibilities, we will develop research that consciously connects to humanistic practices — creation, criticism, education, curation. By moving deliberately among the three positions of 'making,' 'reading,' and 'inspiring,' we aim to present new forms of art in which human sensibility and AI capability complement each other.",
      },
    ],
  },
  // ===================================================================
  {
    slug: "application-development",
    title: "Development Based on Affective AI",
    image: fieldImage("感情AIに基づく開発.png"),
    summary:
      "Development research that implements emotion-reading AI as applied systems and delivers them to society.",
    longDescription:
      "Whether affective AI is truly useful depends on whether it can function safely in psychologically delicate settings. In domains where the parties involved are highly vulnerable — family relationships, mental health, classrooms — implementation calls for the safety, empathy, and calibration of the design more than for the technical accuracy of the model. This domain takes as its object the methodology of implementing emotion-handling AI as applied systems and explores how to design psychologically safe, empathic, and practical feedback.",
    findings:
      "Implementations of affective AI in psychologically delicate domains have yielded design knowledge that goes beyond technical accuracy. A design in which multiple LLM agents with specialist knowledge engage in role-play and multi-stage discussion is effective for producing empathic and practical feedback. At the same time, systems tend to exhibit excessive confidence in their own judgments, and calibration is shown to be indispensable for psychological-support applications.",
    narrative: [
      {
        text:
          "Whether affective AI is truly useful depends on whether it can function safely in psychologically delicate settings. Implementations in domains where the parties involved are highly vulnerable — family relationships, mental health, classrooms, elder care — carry challenges of a different order from lab-based accuracy evaluation. Users stand in a position where they can be deeply harmed by AI judgments, and a mistaken judgment from the AI can damage real human relationships. This domain takes as its object the methodology of implementing emotion-handling AI as applied systems and explores how to design psychologically safe, empathic, and practical feedback.",
      },
      {
        text:
          "AI applications in psychological-support areas face several distinctive difficulties. First, 'clinical safety': there is a risk that erroneous advice from the AI worsens the user's mental state. Second, the necessity of an 'empathic response': what is technically correct is not necessarily emotionally appropriate. Telling a user who reports sadness that 'objective data shows things will improve' may be correct but not appropriate. Third, the limits of 'substituting for experts': AI should not replace licensed professionals but remain in a complementary position. Research in this domain carefully designs the range in which AI can safely contribute, taking these difficulties into account.",
      },
      {
        text:
          "Role-Playing LLM-Based Multi-Agent Support Framework (2025) proposes a system that detects 'suppressed emotion' in a child and 'ideal-parent bias' in a parent from parent–child conversation and returns empathic feedback to each family member. 'Suppressed emotion' refers to feelings the child has toward the parent but cannot directly express, while 'ideal-parent bias' refers to the cognitive bias by which the parent evaluates themselves as an 'ideal parent' and thereby overlooks the child's actual experience. The system is built on 30 Japanese parent–child dialogue scenarios and integrates four processing stages: suppressed-emotion detection, attribute estimation, bias detection, and a five-agent debate.",
        figure: {
          src: "/research-figures/application-development/family-bias.png",
          caption:
            "Overview of the family-communication support framework. A four-stage pipeline from suppressed-emotion detection through multi-agent debate (Role-Playing LLM Multi-Agent, 2025).",
          alt: "Overall diagram of the family-conversation bias-detection multi-agent support framework",
        },
      },
      {
        text:
          "The 'five-agent debate' at the core of this system is a design in which five roles — psychologist, educator, parent role, child role, and moderator — are played by different LLMs, each analyzing and critiquing the conversation from its own standpoint. Having LLMs perform role-play allows the design to structurally surface points that a single perspective overlooks. The psychologist agent contributes psychodynamic insight into suppressed emotion, the educator agent contributes responses suited to developmental stage, the parent-role and child-role agents contribute first-person perspectives, and the moderator integrates them. By mechanically reproducing a discussion among specialists with diverse perspectives, the system produces empathic and practical feedback.",
      },
      {
        text:
          "Evaluation was conducted in two stages. In the first stage, human evaluation, empathy and practicality scored highly. In the second stage, simulation dialogues, signs of reduced suppression and improved mutual understanding were observed in parent–child dialogues after feedback. At the same time, the system exhibited a tendency toward excessive confidence in its own judgments — an important finding that calibration (agreement between confidence and correctness) is indispensable for psychological-support applications. This connects directly to uncertainty research in our lab's interpretability domain and shows the need for dialogue between applied development and basic research.",
      },
      {
        text:
          "Evaluation of affective AI in psychological-support domains has facets that ordinary NLP-task evaluation cannot capture. Beyond technical accuracy (agreement with ground-truth labels), a multifaceted set of indicators is required: (i) empathy (whether the user feels emotionally received), (ii) practicality (whether it leads to concrete behavioral change), (iii) safety (whether the response avoids harming the user), (iv) explainability (whether the system can state why it gives a given piece of advice), and (v) calibration (whether confidence expression is appropriate). This work shows one example of such a multifaceted evaluation framework and makes a pioneering contribution to how affective AI should be evaluated in delicate domains.",
      },
      {
        text:
          "This work offers a methodological template for deploying affective AI to delicate interpersonal domains. Designing the safety and explainability of the system's behavior together with the technology itself is becoming a central concern of implementation research. Going forward we plan to extend beyond family relationships to education, elder care, workplace mental health, and other applied areas. We will advance the social deployment of affective AI in concert with normative debate in the ethics-and-philosophy domain, uncertainty research in the interpretability domain, and the design of relationships in the human–AI interaction domain.",
      },
    ],
  },
  // ===================================================================
  {
    slug: "other-ai-research",
    title: "Other AI Research",
    image: fieldImage("その他AI研究.png"),
    summary:
      "Themes of AI research that are not directly part of affective AI but that our lab pursues.",
    longDescription:
      "Affectosphere Group centers on affective AI, but research in adjacent areas often arises in the course of the work. Generalization of multi-agent design, elucidation of the internal representations of LLMs, and general-purpose foundations for educational and industrial deployment — work that is not directly aimed at emotion but forms the soil of affective AI is gathered here. The question of what world knowledge LLMs draw on, and how, is two sides of the same coin with research on understanding the inside of affective AI, and is a principal concern of this domain.",
    findings:
      "As a way to elicit internal knowledge from LLMs, the property is emerging that associative recall of concrete instances is more reliable than abstract reasoning. Frameworks of parallel recall and voting by multiple agents can achieve higher accuracy than reasoning from a single prompt. Furthermore, on world-knowledge-dependent tasks such as predicting nationality from a name, LLMs surpass conventional neural models at every granularity, confirming the effectiveness of designs that exploit the world knowledge LLMs acquire during pretraining.",
    narrative: [
      {
        text:
          "Affectosphere Group centers on affective AI, but research in adjacent areas often arises along the way. Techniques developed to build affective AI can extend to general problems independent of emotion itself. This domain is the place where general-purpose AI-research themes that branch off from the affective-AI work are gathered. We position research that is not directly aimed at emotion but forms the soil of affective AI — generalization of multi-agent design, elucidation of the internal representations of LLMs, and general-purpose foundations for educational and industrial deployment — here.",
      },
      {
        text:
          "What this domain emphasizes most is the question of how the world knowledge inside LLMs is drawn out. LLMs acquire knowledge about the world from vast amounts of text during pretraining, but drawing on that knowledge requires appropriate prompt design and inference strategies. Capacities such as associative-memory-like chained recall from a cue, reasoning that exploits world knowledge, and elucidation of which forms of knowledge elicitation are reliable are central to deploying LLMs in practice. This is two sides of the same coin with research on the inside of affective AI and constitutes one of the two wheels of our lab's basic research.",
      },
      {
        text:
          "Who Does This Name Remind You of? (LAMA, 2026) is a representative study that analyzed how LLMs draw on internal knowledge. The task is predicting a person's nationality from their name, but the essence of the work is in elucidating 'what knowledge LLMs draw on, and how.' LAMA prompts the LLM to recall 'famous people this name reminds you of' and then estimates the nationality of the original name from the recalled person's nationality. Specifically, two agents — a Person Agent (person recall) and a Media Agent (entertainment and sports recall) — recall famous people in parallel, each estimates a nationality from its recalled set, and a vote produces the final decision. The model achieves an accuracy of 0.817 on 99-country prediction.",
        figure: {
          src: "/research-figures/other-ai-research/lama.png",
          caption:
            "Dual-agent associative-recall architecture of LAMA. The Person Agent and Media Agent recall famous people in parallel, and a vote decides nationality (LAMA, 2026).",
          alt: "Diagram of LAMA's dual-agent associative-recall architecture",
        },
      },
      {
        text:
          "The important finding LAMA delivered is the internal property of LLMs that 'recall of concrete instances is more reliable than abstract reasoning.' Asking 'which country is this name from?' directly is less accurate than asking 'which famous person does this name remind you of?' and inferring nationality from that person. This suggests that LLM knowledge may be stored not as abstract rules but as an associative network of concrete instances. Indirect reasoning that passes through associative memory may be a generally effective strategy for deploying LLMs in practice. The finding extends to a hypothesis for affective-AI internal understanding as well: prompting the model to recall related situations may be more reliable than asking directly for an emotion judgment.",
      },
      {
        text:
          "Nationality and Region Prediction from Names (2026) takes up the same nationality-from-name task as LAMA but develops a more systematic comparison. The work comprehensively compares six conventional neural models (LSTM, Transformer, various embedding methods, etc.) with six LLM prompting strategies (zero-shot, few-shot, chain-of-thought, etc.) at three granularities of nationality, region, and continent. The result is that LLMs surpass conventional neural models at every granularity, and the gap is quantitatively shown to derive from the world knowledge acquired during pretraining.",
        figure: {
          src: "/research-figures/other-ai-research/name-pred.png",
          caption:
            "Systematic comparison of conventional models and LLMs on predicting nationality from names (Nationality and Region Prediction from Names, 2026).",
          alt: "Conceptual comparison of neural models and LLMs for name-to-nationality prediction",
        },
      },
      {
        text:
          "An interesting side finding of this work is that the 'quality of errors' differs between LLMs and neural models. LLM errors tend to be 'misses into nearby regions' — for example, predicting a Japanese name as Vietnamese, a typical East-Asian-region confusion. Neural models, in contrast, err in ways that lean toward high-frequency classes (the United States, China), directly reflecting biases in the training-data distribution. The qualitative difference in error patterns reflects a difference in knowledge structure between the two and provides material for choosing between them in applied design. The work supports the establishment of selection guidelines — LLMs for tasks that require world knowledge, neural models for tasks that exploit the characteristics of training-data distribution.",
      },
      {
        text:
          "Research that gathers in this domain is not directly aimed at affective AI but is continuous with the basic technologies of affective AI. The properties of LLM internal-knowledge elicitation are closely related to uncertainty research on emotion judgment. The methodology of multi-agent design shares design ideas with Kairanban-IBC for emotion recognition and with the five-agent debate for psychological support. This domain functions as a 'reservoir of foundational technology' that accumulates general technical insight branching off from affective AI and feeds it back into affective-AI research. We will continue to accumulate work on themes such as LLMs, multi-agent design, and knowledge elicitation.",
      },
    ],
  },
];
export const aiForScienceImage = fieldImage("AI for Science.png");
