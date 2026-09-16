// Central site metadata so every page/layout pulls from one source of truth.

export const site = {
  name: "Affectosphere Group",
  tagline: "AI時代に、感情でゆとりをつくる。",
  description:
    "Affectosphere Groupは、感情を確率としてとらえ、社会の構造と共に研究することで、誰もが息のしやすい時代を目指すラボです。",
  // English default for the /en subtree. Pages under /en that omit their own
  // description fall back to this instead of the Japanese sentence above.
  descriptionEn:
    "Affectosphere Group studies emotion as a probability distribution and reads it together with the structure of society, working toward a time when everyone can breathe a little easier.",
  affiliation: "関西大学",
  pillars: ["感情コンピューティング", "不確実性", "社会"] as const,
  url: "https://lab.affectosphere.group",
  // Public contact for the principal investigator.
  email: "contact@affectosphere.group",
};

export type NavItem = {
  label: string;
  href: string;
  /** When true this item is shown in the desktop "primary" row.
   *  Items not flagged primary go into the secondary row to keep the
   *  desktop header to two compact rows. */
  primary?: boolean;
};

// Full 11-tab sitemap.  Order matters: this is the order rendered in the
// header, footer, and mobile drawer.
// All nav labels are in English (page content remains Japanese).
// All tabs share the same single navigation row.
// One row, every tab at the same weight.
export const navItems: NavItem[] = [
  { label: "Affectosphere", href: "/affectosphere/" },
  { label: "Research", href: "/research/" },
  { label: "Publications", href: "/publications/" },
  { label: "Column", href: "/column/" },
  { label: "News", href: "/news/" },
  { label: "About", href: "/about/" },
  { label: "Member", href: "/member/" },
  { label: "Awards", href: "/awards/" },
  { label: "Grants", href: "/grants/" },
  { label: "AI for Science", href: "/ai-for-science/" },
  { label: "Services", href: "/services/" },
  { label: "Contact", href: "/contact/" },
];
