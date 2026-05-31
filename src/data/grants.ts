// Competitive grants & research funding received by the PI.
// Sourced from 業績リスト_井下敬翔.docx.

export type Grant = {
  /** Project title (Japanese). */
  projectTitle: string;
  /** Funding program / scheme name. */
  program: string;
  /** Awarding body / 機関. */
  organization?: string;
  /** Period string, e.g. "2025/4 – 2028/3". */
  period: string;
  /** Optional public amount.  Leave undefined when private. */
  amount?: string;
  /** PI / Co-I / 研究代表者 etc. */
  role?: string;
  /** Optional comma-separated co-investigator list. */
  coInvestigators?: string;
};

// Newest start-date first.
export const grants: Grant[] = [
  {
    projectTitle:
      "世界モデルに基づく文脈理解型感情認識マルチエージェントの構築",
    program: "日本財団 HUMAI プログラム 奨励金B",
    organization: "公益財団法人 日本財団",
    period: "2026/8 – 2027/3",
    role: "研究代表者",
  },
  {
    projectTitle:
      "大規模言語モデルにおける感情パラメータの対角化による感情知覚能力の向上",
    program: "次世代研究者挑戦的研究プログラム — 博士後期課程学生の挑戦を支援する —",
    organization: "国立研究開発法人 科学技術振興機構 (JST)",
    period: "2026/4 – 2027/3",
    role: "研究代表者",
  },
  {
    projectTitle:
      "皮肉生成・理解の双方向学習による語用論的推論を強化した大規模言語モデルの構築",
    program: "研究調査助成",
    organization: "公益財団法人 電気通信普及財団",
    period: "2026/4 – 2027/3",
    role: "研究代表者",
    coInvestigators: "上野孝斗, 矢田勝俊",
  },
  {
    projectTitle:
      "感情表現の精緻な制御による人に寄り添う大規模言語モデルの基盤技術に関する研究",
    program: "GMO 研究助成制度",
    organization: "公益財団法人 GMOインターネット財団",
    period: "2026/4 – 2027/3",
    role: "研究代表者",
  },
  {
    projectTitle:
      "ウェアラブルデバイスと AI を活用した感情変化に寄り添うメンタルヘルス支援システムの開発",
    program: "パブリックヘルス科学研究助成金",
    organization: "公益財団法人 パブリックヘルスリサーチセンター",
    period: "2026/4 – 2027/3",
    role: "研究代表者",
  },
  {
    projectTitle:
      "聴覚障害者の運転行動に着目したリスク検知と視覚的支援インターフェースの開発",
    program: "ECOMO 交通バリアフリー研究・活動助成",
    organization: "公益財団法人 交通エコロジー・モビリティ財団",
    period: "2026/4 – 2027/3",
    role: "研究代表者",
  },
  {
    projectTitle:
      "感情データの自給自足による自己進化型感情認識 AI の構築",
    program: "日本財団 HUMAI プログラム 奨励金B",
    organization: "公益財団法人 日本財団",
    period: "2025/8 – 2026/3",
    role: "研究代表者",
  },
  {
    projectTitle:
      "生成 AI による倫理・法的制約を受けない感情データ生成及び、誰もが安心して使える Well-being 支援プラットフォーム",
    program: "〜未踏的な地方の若手人材発掘育成事業〜 LEADING EDGE 四国",
    period: "2025/8 – 2026/1",
    role: "研究代表者",
  },
  {
    projectTitle:
      "職場環境の Well-being 向上を実現する対話型マルチモーダル感情認識システムの構築",
    program: "次世代研究者挑戦的研究プログラム — 博士後期課程学生の挑戦を支援する —",
    organization: "国立研究開発法人 科学技術振興機構 (JST)",
    period: "2025/4 – 2028/3",
    role: "研究代表者",
  },
  {
    projectTitle:
      "職場環境におけるマルチモーダル LLM を用いた感情シミュレーション & ゲーミングによる意思決定支援と組織学習の強化",
    program: "調査研究補助金",
    organization: "公益財団法人 科学技術融合振興財団",
    period: "2025/4 – 2026/3",
    amount: "180,000円",
    role: "研究代表者",
  },
];

export const totalGrants = grants.length;
