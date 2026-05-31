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
      "Graduate School, Kansai University / Center for Data Science and AI Innovation, Shiga University / Japan Safety Society Research Center",
    blurb:
      "Director of the Affectosphere Group. Places the AI-driven understanding, recognition, generation, and expression of human emotion at the center of his research, aiming to realize AI endowed with an EQ that surpasses humans. Pursues collaborations with a diverse range of companies in parallel.",
    portrait: "/people/keito-inoshita.jpg",
    href: "/about/",
  },
];
