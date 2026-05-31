// Lab members.
//
// The lab currently consists of the principal investigator only; the data
// shape here anticipates future researchers, students, and visitors so we
// won't need a schema migration when the lab grows.

export type Role =
  | "Principal Investigator"
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
      "Affectosphere Group を主宰。AI を用いた人間の感情の理解・認識・生成・表出を研究の中心に据え、人間を超える EQ を備えた AI の実現を目指す。多様な企業との連携も並行して進めている。",
    portrait: "/people/keito-inoshita.jpg",
    href: "/about/",
  },
];
