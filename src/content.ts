import { ContentData } from "./types";

export const contentData: ContentData = {
  meta: {
    lastUpdated: "2026-09-15",
    version: "1.0.0"
  },
  contact: {
    coachName: "Leela Madhav",
    phone: "916304895686",
    email: "worldwide.leelamadhav@gmail.com",
    whatsappGroup: "#",
    googleBusiness: "Urban Gliding Hyderabad",
    googleBusinessProfileURL: "#"
  },
  programs: {
    "drop-in": {
      id: "drop-in",
      name: "Drop-in Session",
      displayName: "Drop-in Session",
      price: 599,
      currency: "INR",
      period: "session",
      description: "Intro to fundamentals, ages 5+",
      features: ["Introduction to fundamentals", "Ages 5+ welcome"],
      badge: null,
      ctaText: "Book Session"
    },
    "month-in": {
      id: "month-in",
      name: "Month-in Session",
      displayName: "Month-in Session",
      price: 5999,
      currency: "INR",
      period: "month",
      description: "8 coached classes, unlimited park access, personal progression roadmap",
      features: ["8 coached classes", "Unlimited park access", "Personal progression roadmap"],
      badge: "Featured",
      ctaText: "Enroll Now"
    },
    "residential-standard": {
      id: "residential-standard",
      name: "Residential - Standard",
      displayName: "Residential - Standard",
      price: 4999,
      currency: "INR",
      period: "month",
      description: "8 on-site society classes",
      features: ["8 on-site society classes", "Group learning dynamics", "Convenient doorstep coaching"],
      badge: null,
      ctaText: "Book for Society"
    },
    "residential-plus": {
      id: "residential-plus",
      name: "Residential - Plus",
      displayName: "Residential - Plus",
      price: 6999,
      currency: "INR",
      period: "month",
      description: "8 society classes + 3 skate park sessions",
      features: ["8 on-site society classes", "3 skate park sessions", "Best of both worlds"],
      badge: "Comprehensive",
      ctaText: "Book for Society"
    },
    "vip": {
      id: "vip",
      name: "UGH VIP Skate Plan",
      displayName: "UGH VIP Skate Plan",
      price: 26000,
      currency: "INR",
      period: "flagship",
      description: "Month 1 covers 10 classes and 3 skate park sessions",
      features: ["Doorstep mobile skatepark van", "Curated board + armor kit", "Personalized video vlog"],
      badge: "VIP",
      ctaText: "Inquire About VIP"
    }
  },
  whatsapp: {
    preFillTemplate: "Hi Coach Leela, I want to enroll in {{programName}} (₹{{price}}).",
    freeTrialTemplate: "Hi Coach Leela, I am interested in booking a free residential workshop."
  },
  paymentInstructions: {
    upiId: "ugh@upi",
    steps: ["Scan QR Code", "Enter Amount", "Confirm"]
  },
  emailTemplates: {
    welcomeSubject: "Welcome to UGH",
    welcomeNote: "Thanks for joining!"
  },
  about: {
    description: "Urban Gliding Hyderabad",
    curriculum: []
  },
  leaderboard: {
    lastUpdated: "2026-09-15",
    rankings: {
      kids: [
        { name: "Agasthi", points: 1500, change: "up" },
        { name: "Rahul", points: 1200, change: "same" }
      ],
      adults: [
        { name: "Tribhuvan", points: 2000, change: "up" },
        { name: "Ronnie", points: 1800, change: "down" }
      ]
    }
  }
};
