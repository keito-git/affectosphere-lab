// Lab members.
//
// The lab currently consists of the principal investigator only; the data
// shape here anticipates future researchers, students, and visitors so we
// won't need a schema migration when the lab grows.

export type Role =
  | "Principal Investigator"
  | "Member"
  | "Postdoctoral Researcher"
  | "Doctoral Student"
  | "Master's Student"
  | "Undergraduate"
  | "Visiting Researcher"
  | "Collaborator";

export type Person = {
  slug: string;
  name: string;
  nameJa?: string;
  role: Role;
  affiliation: string;
  /** One-line bio shown on the Member grid. */
  blurb: string;
  /** Optional path to a portrait image under /public.  Leave undefined to render initials. */
  portrait?: string;
  /** Optional link to a personal page (defaults to /about for the PI). */
  href?: string;
};

export const members: Person[] = [
  {
    slug: "keito-inoshita",
    name: "Keito Inoshita",
    nameJa: "井下 敬翔",
    role: "Principal Investigator",
    affiliation:
      "関西大学大学院 / 滋賀大学 DS・AI研究推進センター / 日本セーフティソサイエティ研究センター",
    blurb:
      "AI に感情知能を与える研究をしている。感情の読み取りから保持・推論・生成・相互作用・社会への定着までを Computational Affective Intelligence（CAI）というひと続きの体系として構築中。Affectosphere Group 主宰。見据えるのは、人間を超える EQ を備えた AI である。",
    portrait: "/people/keito-inoshita.jpg",
    href: "/about/",
  },
  {
    slug: "toma-okugawa",
    name: "Toma Okugawa",
    nameJa: "奥河 董馬",
    role: "Member",
    affiliation: "弓削商船高等専門学校 情報工学科",
    blurb:
      "Small Language Model（SLM）を用いた地域課題の解決に取り組む。",
    portrait: "/people/okugawa-toma.jpg",
    href: "https://t-okugawa.dev/",
  },
];
