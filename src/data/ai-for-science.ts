// AI for Science page content.
// Mirrors the structure of research-domains.ts NarrativeBlock for visual
// consistency with the affective-AI research detail pages.

export type NarrativeBlock = {
  /** Optional sub-section heading (rendered above the paragraph). */
  heading?: string;
  text: string;
  figure?: {
    src: string;
    caption: string;
    alt: string;
  };
};

export const aiForScienceLongDescription =
  "AI for Science とは、AI を新しい観測装置として科学に持ち込み、これまで経験と主観に依存していた知識生産を、計量的で再現可能な手続きに置き換える営みである。Affectosphere Group は教育学・政治学・生態学・法律学をはじめ、文理を横断する領域の研究者と共同し、感情AI研究で培った「人間判断の揺らぎをデータとして扱う技法」を、それぞれの分野の問いに持ち出している。";

export const aiForScienceFindings =
  "分野をまたいで繰り返し現れるのは、LLM が「平均的にもっともらしい出力」を高い品質で生成する一方、分布の端——希少な議論、少数派の国、ロングテールの命名、領域固有の細則——を体系的に取り落とすという構造である。AI for Science は手法の応用ではなく、分野ごとに「何を任せられて、何を任せてはならないか」を見極める営みになっている。";

// Inquiry endpoint (the form opens the user's email client with this address).
export const inquiryEmail = "inquiry@affectosphere.group";

export const aiForScienceNarrative: NarrativeBlock[] = [
  {
    text: "AI を分析器として使うことは、分析器そのものの偏りという新しい妥当性問題を生む。だから AI for Science では、成果と同じくらい、評価の方法論そのものが研究対象になる。",
  },
  {
    heading: "教育学 × AI",
    text: "生成AIは文章の品質を大きく押し上げる一方、主張の希少性は人間の約5分の1にとどまり、論の結合構造の分散を7割前後も奪う。ライティング評価は「うまく書けたか」から「他者と違う考え方ができているか」へ移るべきだと主張している。",
  },
  {
    heading: "政治学 × AI",
    text: "20万件規模の日本語ツイートの感情分析と、国名を入れ替えたときに予測がどれだけ反転するかの計測から、LLM に埋め込まれた国家バイアスを定量化した。大規模学習コーパスを走査すると、その偏りが学習データの段階で既に入っていることも見える。",
  },
  {
    heading: "生態学 × AI",
    text: "クモ 48,464 種の学名を対象に、語源の自動分類を LLM で評価した。形態や地理に由来する命名では人手に近い精度に達する一方、生態・行動や文化に由来する命名では大きく落ちる——どこまで任せられるかの境界が、そこに出る。",
  },
  {
    heading: "法律学 × AI",
    text: "宅地建物取引士試験の過去10回分を解かせたところ、いずれのモデルも合格水準には届かなかった。完全な代替の段階にはないが、学習者支援や法務補助としては有望である、という線が引ける。",
  },
  {
    text: "感情AIで磨いた診断の技法を、社会的に意義のある問いへ持ち出す場であると同時に、領域の専門家との往復のなかで感情AI側の方法論を鍛え直す場でもある。",
  },
];
